import time, hashlib, random


def make_codes():
  print("Making 7 codes")
  current_date = int(time.time() / (24 * 60 * 60))
  all_hashes = []
  for i in range(7):
    random_code = round(random.random(), 5)
    combined_pre_hash = str(current_date + random_code)
    hash = hashlib.md5(combined_pre_hash.encode()).hexdigest()
    all_hashes.append(hash)
    print(current_date, random_code)
    print(hash)
    current_date += 1
  print(str(all_hashes))


def check_code(random_code):
  current_date = int(time.time() / (24 * 60 * 60))
  combined_pre_hash = str(current_date + random_code)
  return hashlib.md5(combined_pre_hash.encode()).hexdigest()


def check_date():
  return int(time.time() / (24 * 60 * 60))
