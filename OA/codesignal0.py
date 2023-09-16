class CloudStorageSystemOld:
    def __init__(self):
        self.files = {}

    def add_file(self, name, size):
        if name in self.files:
            return"false"
        self.files[name] = int(size)
        return "true"

    def copy_file(self, name_from, name_to):
        if name_from not in self.files or name_to in self.files:
            return "false"
        self.files[name_to] = self.files[name_from]
        return "true"

    def get_file_size(self, name):
        if name not in self.files:
            return ""
        return str(self.files[name])

    def find_file(self, perfix, suffix):
        result = []
        for file, size in self.files.items():
            if perfix == file[:len(perfix)] and suffix == file[len(file) - len(suffix):]:
                result.append([file, size])
        s = []
        if len(result) == 0:
            return ""
        for file, size in sorted(result, key=lambda x: (-1 * x[1], x[0])):
            s.append(file + "(" + str(size) + ")")
        return ", ".join(s)


class CloudStorageSystem:
    def __init__(self):
        self.files = {}
        self.users = {"admin": [float("inf"), 0, []]}

    def add_file(self, name, size):
        res = self.add_file_by("admin", name, size)
        return "false" if res == "" else "true"

    def copy_file(self, name_from, name_to):
        if name_from not in self.files or name_to in self.files:
            return "false"
        user_id = self.files[name_from][1]
        self.files[name_to] = self.files[name_from]
        self.users[user_id][2].append(name_to)
        return "true"

    def get_file_size(self, name):
        if name not in self.files:
            return ""
        return str(self.files[name][0])

    def find_file(self, perfix, suffix):
        match_files = []
        for file, [size, _] in self.files.items():
            if perfix == file[:len(perfix)] and suffix == file[len(file) - len(suffix):]:
                match_files.append([file, size])
        result = []
        if len(match_files) == 0:
            return ""
        for file, size in sorted(match_files, key=lambda x: (-1 * x[1], x[0])):
            result.append(file + "(" + str(size) + ")")
        return ", ".join(result)

    def add_user(self, user_id, capacity):
        if user_id in self.users:
            return "false"
        self.users[user_id] = [int(capacity), 0, []]
        return "true"

    def add_file_by(self, user_id, name, size):
        size = int(size)
        if name in self.files:
            return ""
        if user_id not in self.users:
            return ""
        if self.users[user_id][1] + size > self.users[user_id][0]:
            return ""
        self.users[user_id][1] += size
        self.users[user_id][2].append(name)
        self.files[name] = [size, user_id]
        return str(self.users[user_id][0] - self.users[user_id][1])

    def update_capacity(self, user_id, capacity):
        if user_id not in self.users:
            return ""
        if self.users[user_id][1] <= capacity:
            return "0"

        rm_files = 0
        files_of_user = []
        for file in self.users[user_id][2]:
            size = self.files[file][0]
            files_of_user.append([file, size])
        tmp = sorted(files_of_user, key=lambda x: (-1 * x[1], x[0]))
        self.users[user_id][0] = capacity
        while self.users[user_id][0] < self.users[user_id][1]:
            self.users[user_id][1] -= tmp[rm_files][1]
            self.users[user_id][2].remove(tmp[rm_files][0])
            rm_files += 1
        return str(rm_files)


def solution(queries):
    css = CloudStorageSystem()
    result = []
    for query in queries:
        if query[0] == "ADD_FILE":
            result.append(css.add_file(query[1], query[2]))
        elif query[0] == "COPY_FILE":
            result.append(css.copy_file(query[1], query[2]))
        elif query[0] == "GET_FILE_SIZE":
            result.append(css.get_file_size(query[1]))
        elif query[0] == "FIND_FILE":
            result.append(css.find_file(query[1], query[2]))
        elif query[0] == "ADD_USER":
            result.append(css.add_user(query[1], query[2]))
        elif query[0] == "ADD_FILE_BY":
            result.append(css.add_file_by(query[1], query[2], query[3]))
        elif query[0] == "UPDATE_CAPACITY":
            result.append(css.update_capacity(query[1], query[2]))
    return result