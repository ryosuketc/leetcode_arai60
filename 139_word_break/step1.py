class SolutionWA:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        words = set(wordDict)
        def word_break_start_from(index):
            print(f"index={index}")
            if index == len(s):
                return True
            is_breakable = False
            for word in words:
                print(f"word={word}")
                print(f"s[index:]={s[index:]}, index={index}, s[index:].startswith(word, index)={s[index:].startswith(word, index)}")
                print(s[index:].startswith(word, index))
                if not s[index:].startswith(word, index):
                    continue
                if word_break_start_from(index + len(word)):
                    is_breakable = True
            return is_breakable

        return word_break_start_from(0)



class SolutionTLE:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        words = set(wordDict)
        def word_break_start_from(index):
            if index == len(s):
                return True
            is_breakable = False
            for word in words:
                if not s.startswith(word, index):
                    continue
                if word_break_start_from(index + len(word)):
                    is_breakable = True
            return is_breakable

        return word_break_start_from(0)


class SolutionAC:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        words = set(wordDict)
        memo = {}
        def word_break_start_from(index):
            if index == len(s):
                return True
            if index in memo:
                return memo[index]

            is_breakable = False
            for word in words:
                if not s.startswith(word, index):
                    continue
                if word_break_start_from(index + len(word)):
                    is_breakable = True
            memo[index] = is_breakable
            return memo[index]

        return word_break_start_from(0)
