class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        result = []
        digi_logs = []
        letter_logs = []
        for i in range(len(logs)):
            temp = list(logs[i].split(" "))
            if(temp[1].isdigit()):
                digi_logs.append(logs[i])
            else:
                letter_logs.append(temp)
        sorted_letter_logs = sorted(letter_logs, key=lambda x: (x[1:], x[0]))
        sorted_letter_logs_list = []
        for i in sorted_letter_logs:
            s = ' '.join(i)
            sorted_letter_logs_list.append(s)
        result.extend(sorted_letter_logs_list)
        result.extend(digi_logs)
        return result