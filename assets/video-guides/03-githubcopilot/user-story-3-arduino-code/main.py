"""Microcontroller simulator demo for video recording.

This script mimics a tiny Arduino-style board with:
- setup() / loop() structure
- digital pins
- a simulated analog temperature sensor
- serial-style logging

It is intentionally lightweight so it can be run live during a demo without
extra dependencies.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from math import sin
from random import Random
from time import sleep


LED_PIN = 13
BUZZER_PIN = 9
TEMP_SENSOR_PIN = 0


@dataclass
class SerialMonitor:
	"""Collect and print messages like an Arduino serial monitor."""

	history: list[str] = field(default_factory=list)

	def println(self, message: str) -> None:
		entry = f"[{datetime.now().strftime('%H:%M:%S')}] {message}"
		self.history.append(entry)
		print(entry)


@dataclass
class MicrocontrollerSimulator:
	"""Tiny board simulator with a few digital pins and one sensor."""

	serial: SerialMonitor = field(default_factory=SerialMonitor)
	rng: Random = field(default_factory=lambda: Random(7))
	pin_modes: dict[int, str] = field(default_factory=dict)
	digital_pins: dict[int, bool] = field(default_factory=dict)
	temperature_celsius: float = 22.0
	cycle: int = 0

	def pin_mode(self, pin: int, mode: str) -> None:
		self.pin_modes[pin] = mode

	def digital_write(self, pin: int, value: bool) -> None:
		self.digital_pins[pin] = value

	def analog_read(self, pin: int) -> int:
		if pin != TEMP_SENSOR_PIN:
			return 0

		drift = sin(self.cycle / 3.0) * 3.5
		noise = self.rng.uniform(-0.7, 0.7)
		self.temperature_celsius = 22.0 + drift + noise

		# Convert the simulated temperature to a 10-bit ADC value.
		return int(max(0, min(1023, (self.temperature_celsius / 50.0) * 1023)))

	def read_temperature(self) -> float:
		raw_value = self.analog_read(TEMP_SENSOR_PIN)
		return round((raw_value / 1023.0) * 50.0, 1)

	def setup(self) -> None:
		self.pin_mode(LED_PIN, "OUTPUT")
		self.pin_mode(BUZZER_PIN, "OUTPUT")
		self.serial.println("Booting microcontroller simulator...")
		self.serial.println("Pins ready: LED on D13, buzzer on D9, sensor on A0")

	def loop(self) -> None:
		self.cycle += 1
		temperature = self.read_temperature()

		led_state = temperature >= 24.0
		buzzer_state = temperature >= 26.5

		self.digital_write(LED_PIN, led_state)
		self.digital_write(BUZZER_PIN, buzzer_state)

		led_text = "ON" if led_state else "OFF"
		buzzer_text = "ON" if buzzer_state else "OFF"

		self.serial.println(
			f"cycle={self.cycle:02d} temp={temperature:04.1f}C led={led_text} buzzer={buzzer_text}"
		)

	def run(self, cycles: int = 12, delay_seconds: float = 0.4) -> None:
		self.setup()
		for _ in range(cycles):
			self.loop()
			sleep(delay_seconds)


def main() -> None:
	board = MicrocontrollerSimulator()
	board.run()


if __name__ == "__main__":
	main()
