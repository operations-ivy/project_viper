log_dir = "/home/zaphod/code/sample_logs"

auth_log = log_dir + "/auth.log"
boot_log = log_dir + "/boot.log"
messages_log = log_dir + "/messages"

known_logs= [auth_log, boot_log, messages_log]
all_logs = "/home/zaphod/code/sample_logs/*"

read_auth_log = open(auth_log, "r")
line_sum = 0
for line in read_auth_log:
    line = line.lower()
    if "ron" in line:
        line_sum = line_sum + 1
read_auth_log.close()

print(line_sum)

read_auth_log = open(auth_log, "r")
ron_count = 0
for line in read_auth_log:
    line = line.lower()
    ron_count = line.count("ron")
read_auth_log.close()

print(ron_count)