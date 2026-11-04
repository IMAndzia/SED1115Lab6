# Submit this file via brightspace

# You should not modify the signature (name, input, return type) of this function
def translate(angle: float) -> int:
	"""
	Converts an angle in degrees to the corresponding input
	for the duty_u16 method of the servo class
"""

	# Clamp angle to valid servo range [0, 180] to handle out-of-bounds test cases safely
	angle = max(0.0, min(180.0, angle))
	
	# Calculate pulse width in microseconds (500us for 0°, 2500us for 180°)
	pulse_width = 500 + (2000 * angle / 180)
	
	# Convert pulse width to 16-bit duty cycle integer (0 to 65535 based on 20,000us period)
	duty_u16_val = int((pulse_width / 20000) * 65535)
	
	return duty_u16_val