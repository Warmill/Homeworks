# SyntaxError
# TypeError
# ValueError
# KeyError
# NameError
import logging
logging.basicConfig(filename="logs.log", encoding="UTF-8", level=logging.DEBUG)

logging.info("Program start working!")
try:
    logging.warning("Started to work on risky code")
    print(a)
except TypeError:
    logging.error("TypeError")
except NameError:
    logging.error("NameError")