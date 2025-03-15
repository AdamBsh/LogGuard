import re
import sys
from collections import defaultdict
import datetime
import os

def analyze_log_file(log_file, threshold=3):
    failed_attempts = defaultdict(list)
    
    try:
        if not os.path.exists(log_file):
            print("File not found:", log_file)
            return None
            
        with open(log_file, 'r') as f:
            for line in f:
                if "Failed login attempt" in line:
                    match = re.search(r'from IP (\d+\.\d+\.\d+\.\d+)', line)
                    if match:
                        ip = match.group(1)
                        date = line.split()[0] + " " + line.split()[1]
                        failed_attempts[ip].append(date)
    except Exception as e:
        print("Error:", str(e))
        return None
    
    return failed_attempts

def generate_report(failed_attempts, threshold, log_file):
    print("===== LOGGUARD SECURITY REPORT =====")
    print("Analysis Date: {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print("File analyzed: {}".format(log_file))
    print("Alert threshold: {} attempts\n".format(threshold))
    
    suspicious_ips = {}
    for ip, attempts in failed_attempts.items():
        if len(attempts) >= threshold:
            suspicious_ips[ip] = len(attempts)
    
    if suspicious_ips:
        print("ALERT: {} suspicious IP(s) detected!\n".format(len(suspicious_ips)))
        
        for ip, count in sorted(suspicious_ips.items(), key=lambda x: x[1], reverse=True):
            print("IP: {} - {} failed login attempts".format(ip, count))
            print("  First attempt: {}".format(failed_attempts[ip][0]))
            print("  Last attempt: {}".format(failed_attempts[ip][-1]))
            print("")
    else:
        print("No suspicious activity detected.\n")
    
    print("Total IPs analyzed: {}".format(len(failed_attempts)))
    total_attempts = sum(len(attempts) for attempts in failed_attempts.values())
    print("Total failed attempts: {}".format(total_attempts))
    print("====================================")

def main():
        
    log_file = sys.argv[1]
    threshold = 3 
    
    failed_attempts = analyze_log_file(log_file, threshold)
    
    if failed_attempts is not None:
        generate_report(failed_attempts, threshold, log_file)

if __name__ == "__main__":
    main()