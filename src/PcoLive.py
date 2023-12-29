import asyncio
import sys
from ProPresenter import get_current_index
from utils import get_pco, setup_logger
import atexit


def exit_handler(service_type_id, plan_id):
    pco = get_pco()
    pco.post(f"/services/v2/service_types/{service_type_id}/plans/{plan_id}/live/toggle_control")
    logger.info("Releasing Control")


logger = setup_logger(__name__)


def choose_live(service_type_id=None, plan_id=None):
    """
    :param service_type_id: str, Optional. The ID of the service type.
    :param plan_id: str, Optional. The ID of the plan.
    :return: dict. A dictionary with the selected service type ID and plan ID.
    """
    if service_type_id and plan_id:
        return {"plan_id": plan_id, "service_type_id": service_type_id}

    try:
        pco = get_pco()
    except Exception as e:
        logger.error(e)
        sys.exit()
    service_type_list = []
    service_types = pco.iterate("/services/v2/service_types")
    for service_type in service_types:
        service_type_list.append((service_type['data']["id"], service_type['data']['attributes']["name"]))
    for i, (service_type_id, service_type_name) in enumerate(service_type_list):
        print(f"{i + 1}. {service_type_name}")

    service_type_number = int(input("Select the service type by entering a number: "))
    selected_service_type_id = service_type_list[service_type_number - 1][0]
    logger.info(f"Selected service type id is {selected_service_type_id}")

    plans_list = []

    plans = pco.iterate(f"/services/v2/service_types/{selected_service_type_id}/plans?filter=future")
    for plan in plans:
        if plan['data']['attributes']["title"]:
            plans_list.append((plan['data']["id"],
                               f'{plan["data"]["attributes"]["title"]} - {plan["data"]["attributes"]["dates"]}'))
        else:
            plans_list.append((plan['data']["id"], plan['data']['attributes']["dates"]))

    for i, (plan_id, plan_name) in enumerate(plans_list):
        print(f"{i + 1}. {plan_name}")

    plan_number = int(input("Select the plan by entering a number: "))
    selected_plan_id = plans_list[plan_number - 1][0]
    logger.info(f"Selected plan id is {selected_plan_id}")

    return {"plan_id": selected_plan_id,
            "service_type_id": selected_service_type_id}


def get_current_set_list(service_type_id, plan_id, display=False):
    pco = get_pco()
    live_data = pco.get(f"/services/v2/service_types/{service_type_id}/plans/{plan_id}/live?"
                        f"include=items,controller,next_item_time")
    if display:
        # pprint(live_data["included"])
        if live_data["data"]['attributes']['title']:
            logger.info(f" - {live_data['data']['attributes']['title']}")
        for item in live_data["included"]:
            if item['type'] == 'Item':
                logger.info(f"{item['attributes']['sequence'] - 1} - {item['attributes']['title']}")


def get_current_live_status(service_type_id, plan_id, display=False):
    pco = get_pco()
    current_item = pco.get(f"/services/v2/service_types/{service_type_id}/plans/"
                           f"{plan_id}/live/?include=current_item_time,items")
    if not current_item["data"]['links']['controller']:
        """We need to take control if the service hasn't started"""
        pco.post(f"/services/v2/service_types/{service_type_id}/plans/{plan_id}/live/toggle_control")
        pco.post(f'/services/v2/service_types/{service_type_id}/plans/{plan_id}/live/go_to_next_item')

        current_item = pco.get(f"/services/v2/service_types/{service_type_id}/plans/"
                               f"{plan_id}/live/?include=current_item_time,items")

    item_id = None
    item_name = None
    sequence = None
    # pprint(current_item)
    try:
        for include in current_item['included']:
            # pprint(include)

            if include['type'] == 'ItemTime':
                item_id = include['relationships']['item']['data']['id']
            if include['type'] == 'Item' and include['id'] == item_id:
                sequence = include['attributes']['sequence'] - 1
                item_name = include['attributes']['title']

        live_status = {
            "title": current_item["data"]['attributes']['title'],
            "date": current_item["data"]['attributes']['dates'],
            "sequence": sequence,
            "item_name": item_name
        }
        if display:
            logger.info("Current PCO Item Status:\n")
            for stat, data in live_status.items():
                logger.info(f"{stat}: {data}")

        return live_status
    except Exception as e:
        logger.info("ProPresenter is Clear")


def get_index(service_type_id, plan_id):
    pco = get_pco()
    index = 0
    while True:
        pco_live_status = get_current_live_status(service_type_id, plan_id)
        # print(pco_live_status)

        pro_presenter_status = asyncio.run(get_current_index())
        if pro_presenter_status:

            if pco_live_status["sequence"] == pro_presenter_status['sequence'] and pco_live_status["date"] == \
                    pro_presenter_status['date']:
                logger.info("PCO and ProPresenter are in sync.")
            else:
                logger.info("PCO and ProPresenter are not in sync.")
                logger.info(f"PCO: {pco_live_status['sequence']}, ProPresenter: {pro_presenter_status['sequence']}")
                try:
                    index = pro_presenter_status['sequence'] - pco_live_status['sequence']
                except Exception as e:
                    logger.error(e)
                if index < 0:
                    logger.info(f"{pro_presenter_status['sequence'] - pco_live_status['sequence']} - Click Back")
                    pco.post(f'/services/v2/service_types/{service_type_id}/plans/{plan_id}/live/go_to_previous_item')
                else:
                    logger.info(f"{pro_presenter_status['sequence'] - pco_live_status['sequence']} - Click Forward")
                    pco.post(f'/services/v2/service_types/{service_type_id}/plans/{plan_id}/live/go_to_next_item')
                # print(pro_presenter_status['sequence'] - pco_live_status['sequence'])

        else:
            logger.info("Pro Presenter is Clear")


# if __name__ == '__main__':
#     try:
#         config = choose_live()
#         atexit.register(exit_handler, config['service_type_id'], config['plan_id'])
#         get_index(config['service_type_id'], config['plan_id'])
#     except KeyboardInterrupt:
#         logger.info("Thanks for using this recipe. Check out more recipes at https://pcochef.com")
