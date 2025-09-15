import random
import copy

# ========================== Cấu hình chung
days = ["T2", "T3", "T4", "T5", "T6", "T7"]
cas = ["Ca 1", "Ca 2", "Ca 3", "Ca 4"]
SLOTS_PER_WEEK = len(days) * len(cas)
MAX_TRIES = 2000
ROOMS = [f"P{i:03d}" for i in range(1, 31)]

# ========================== Kiểm tra slot hợp lệ
def valid_slot(slot, ses, schedule):
    for s in schedule.get(slot, []):
        if (
            s["room"] == ses["room"]
            or s["teacher"] == ses["teacher"]
            or s["class"] == ses["class"]
        ):
            return False
    return True

# ========================== Mở rộng buổi học
def expand_sessions(sessions):
    expanded = []
    for cls, subj, teacher, count in sessions:
        for i in range(count):
            expanded.append({
                "class": cls,
                "subject": subj,
                "teacher": teacher,
                "room": random.choice(ROOMS),
                "name": f"{cls}-{subj} ({i+1}) - {teacher}"
            })
    return expanded

# ========================== Sinh lịch ngẫu nhiên
def random_schedule(sessions):
    expanded = expand_sessions(sessions)
    schedule = {(d, c): [] for d in days for c in cas}

    for ses in expanded:
        placed = False
        for _ in range(MAX_TRIES):
            slot = (random.choice(days), random.choice(cas))
            if valid_slot(slot, ses, schedule):
                schedule[slot].append(ses)
                placed = True
                break
        if not placed:
            raise ValueError(
                f"Không thể xếp session '{ses['name']}' vào slot hợp lệ."
            )
    return schedule

# ========================== Đánh giá lịch
def evaluate(schedule):
    score = 0
    day_count = {d: 0 for d in days}
    ca_count = {c: 0 for c in cas}
    teacher_slots = {}

    for (d, c), lst in schedule.items():
        day_count[d] += len(lst)
        ca_count[c] += len(lst)
        for ses in lst:
            teacher_slots.setdefault(ses["teacher"], []).append((d, c))

    for d in days:
        if day_count[d] > 0: score += 10
        else: score -= 10
        if day_count[d] > 4: score -= (day_count[d] - 4) * 5
        if day_count[d] == len(cas): score -= 8

    avg = sum(ca_count.values()) / len(cas)
    variance = sum((c - avg) ** 2 for c in ca_count.values())
    score -= variance * 0.5

    ca_index = {c: i for i, c in enumerate(cas)}
    for teacher, slots in teacher_slots.items():
        slots_by_day = {}
        for d, c in slots:
            slots_by_day.setdefault(d, []).append(ca_index[c])
        for d, idxs in slots_by_day.items():
            idxs.sort() 
            for i in range(len(idxs) - 2):
                if idxs[i+2] - idxs[i] == 2 and idxs[i+1] - idxs[i] == 1:
                    score -= 10
            has_consecutive = any(idxs[i+1] - idxs[i] == 1 for i in range(len(idxs) - 1))
            if not has_consecutive:
                score += 5
    return score

# ========================== Helper
def build_ses_to_slot(schedule):
    m = {}
    for slot, lst in schedule.items():
        for ses in lst:
            m[ses["name"]] = slot
    return m

# ========================== Sinh neighbor
def neighbor(schedule, sessions):
    expanded = expand_sessions(sessions)
    new_schedule = {slot: list(lst) for slot, lst in schedule.items()}
    ses_to_slot = build_ses_to_slot(new_schedule)

    ses = random.choice(expanded)
    old_slot = ses_to_slot.get(ses["name"])
    if old_slot is None:
        return new_schedule

    new_schedule[old_slot] = [s for s in new_schedule[old_slot] if s["name"] != ses["name"]]

    placed = False
    for _ in range(MAX_TRIES):
        slot = (random.choice(days), random.choice(cas))
        if valid_slot(slot, ses, new_schedule):
            new_schedule[slot].append(ses)
            placed = True
            break
    if not placed:
        new_schedule[old_slot].append(ses)
    return new_schedule

# ========================== Hill Climbing
def hill_climbing(sessions, iterations=1000):
    current = random_schedule(sessions)
    current_score = evaluate(current)
    best = copy.deepcopy(current)
    best_score = current_score

    for _ in range(iterations):
        nxt = neighbor(current, sessions)
        nxt_score = evaluate(nxt)
        if nxt_score >= current_score:
            current, current_score = nxt, nxt_score
        if current_score > best_score:
            best, best_score = copy.deepcopy(current), current_score
    return best

def random_restart_hill_climbing(sessions, restarts=10, iterations=1000):
    best_overall, best_score = None, None
    for _ in range(restarts):
        candidate = hill_climbing(sessions, iterations)
        score = evaluate(candidate)
        if best_overall is None or score > best_score:
            best_overall, best_score = candidate, score
    return best_overall, best_score
