from dataclasses import dataclass
from functools import cached_property

@dataclass
class Robot:
    
    environment: str 
    
    @cached_property
    def amplifier(self):
        from app.robot import Amplifier
        return Amplifier()
    
    @cached_property
    def servo(self):
        from app.robot import Servo
        return Servo(amplifier=self.amplifier)
    
    @cached_property
    def controller(self):
        from app.robot import Controller
        return Controller()
    
    @cached_property
    def settings(self):
        from app.robot import Settings
        return Settings(environment=self.environment)

