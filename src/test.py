
import traceback

def coco(tee):
    priddnt(tee)

try:
    print(coco('coco'))

except Exception as error:

    print(f'ERROR: {traceback.format_exc()}')