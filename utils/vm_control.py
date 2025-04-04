import subprocess

def control_vm(action: str):
    try:
        if action == "start":
            subprocess.run("Start-VM 'MyVM'", shell=True)
        elif action == "stop":
            subprocess.run("Stop-VM 'MyVM'", shell=True)
        return {"status": f"VM {action} issued"}
    except Exception as e:
        return {"error": str(e)}
