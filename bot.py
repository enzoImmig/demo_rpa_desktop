# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

from pywinauto import Application

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    try:
        app = Application(backend="uia").connect(path=r"C:\Program Files\Fakturama2\Fakturama.exe")
        app.kill()
    except:
        print("Failed to kill applications")

    app = Application(backend="uia").start(r"C:\Program Files\Fakturama2\Fakturama.exe")
    window = app.window(title_re="Fakturama.*", control_type="Window")
    window.maximize()


    window.window(title="New product").click_input()
    
    window.print_control_identifiers(filename="elements_tree.txt")

    window.window(title="Item Number", control_type="Edit").set_text("123")
    window.window(title="Name", control_type="Edit").set_text("123")
    window.window(title="Category", control_type="Edit").set_text("123")
    window.window(title="supplier code", control_type="Edit").set_text("123")
    #window.window(title="Price (gross)", control_type="Edit").set_text("123")
    #window.window(title="cost price (net)", control_type="Edit").set_text("123")


    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK.",
    #     total_items=0,
    #     processed_items=0,
    #     failed_items=0
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()