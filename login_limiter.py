import time

CORRECT_USER = "admin"
CORRECT_PASS = "Pass@123"
MAX_TRIES = 3
LOCK_SECONDS = 15

failed_tries = 0
locked_until = 0.0

print("=== Login Attempt Control System ===")

while True:
    now = time.time()
    if now < locked_until:
        wait_time = int(locked_until - now) + 1
        print(f"[BLOCKED] Too many failed attempts. Wait {wait_time}s...")
        time.sleep(1)
        continue

    user = input("Username (or 'q' to quit): ").strip()
    if user.lower() == "q":
        break

    password = input("Password: ").strip()

    if user == CORRECT_USER and password == CORRECT_PASS:
        print("[SUCCESS] Login allowed! Access granted.")
        failed_tries = 0
        break

    failed_tries += 1
    if failed_tries >= MAX_TRIES:
        locked_until = time.time() + LOCK_SECONDS
        failed_tries = 0
        print(f"[LOCKED] {MAX_TRIES} failed attempts. Access restricted for {LOCK_SECONDS} seconds.")
    else:
        left = MAX_TRIES - failed_tries
        print(f"[DENIED] Wrong credentials. {left} attempt(s) left before lock.")
