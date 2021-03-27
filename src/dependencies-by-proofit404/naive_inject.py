from app.robot import Robot, Servo, Amplifier, Controller, Settings

@dataclass
class Robot:
    
    servo: Servo
    controller: Controller
    settings: Settings 
    

def inject():
    robot = Robot(
        servo=Servo(amplifier=Amplifier()),
        controller=Controller(),
        settings=Settings(environment="production")
        )

