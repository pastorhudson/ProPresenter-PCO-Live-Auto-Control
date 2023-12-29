import argparse
import atexit
from PcoLive import choose_live, exit_handler, get_index
from utils import setup_logger
from pypco.exceptions import PCORequestException


def main():
    logger = setup_logger(__name__)
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", help="test option: return the string 'SUCCESS'", action='store_true')
    parser.add_argument("-s", "--service_type_id", help="service type id")
    parser.add_argument("-p", "--plan_id", help="plan id")

    args = parser.parse_args()

    if args.test:
        print("SUCCESS")
        return
    try:
        if args.service_type_id and args.plan_id:
            config = choose_live(args.service_type_id, args.plan_id)
            atexit.register(exit_handler, config['service_type_id'], config['plan_id'])
            get_index(config['service_type_id'], config['plan_id'])

        else:
            config = choose_live()
            atexit.register(exit_handler, config['service_type_id'], config['plan_id'])
            get_index(config['service_type_id'], config['plan_id'])
    except KeyboardInterrupt:
        logger.info("Thanks for using this recipe. Check out more recipes at https://pcochef.com")
    except PCORequestException:
        logger.error("Please Check your Planning Center API keys are correct in the config.ini")



if __name__ == "__main__":
    main()
