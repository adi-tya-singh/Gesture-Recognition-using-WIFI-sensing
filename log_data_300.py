import serial

def log_serial_data(port, baudrate, output_file, samples_per_instance=300):
    try:
        with serial.Serial(port, baudrate, timeout=1) as ser, open(output_file, 'wb') as file:
            print(f"Connected to {port} at {baudrate} baud.")
            print("Listening for data... Press Ctrl+C to stop.")
            
            sample_count = 0  # Initialize sample counter
            instance_number = 1
            while True:
                try:
                    # Read raw bytes from the serial port
                    raw_line = ser.readline()
                    
                    # Check if the line contains the keyword `CSI_DATA`
                    if b'CSI_DATA' in raw_line:
                        # Write the raw line to the output file
                        file.write(raw_line)
                        file.flush()  # Ensure data is written immediately

                        # Increment the sample count
                        sample_count += 1

                        # After 300 samples, write "new instance" to the file and reset count
                        if sample_count >= samples_per_instance:
                            instance_message = f"new instance {instance_number}\n".encode('utf-8')  # Encode string to bytes
                            file.write(instance_message)  # Write instance info as bytes
                            file.flush()
                            print(f"new {instance_number}")  # Print to console with instance number
                            sample_count = 0  # Reset the sample count
                            instance_number += 1  # Increment the instance number
                except KeyboardInterrupt:
                    print("\nData logging stopped by user.")
                    break
    except Exception as e:
        print(f"Error: {e}")

# Configuration
PORT = "COM7"          # Adjust if using a different port
BAUDRATE = 921600
OUTPUT_FILE = "csi_data_clap_v1.3"

log_serial_data(PORT, BAUDRATE, OUTPUT_FILE)
