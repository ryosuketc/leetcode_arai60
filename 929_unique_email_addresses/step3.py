class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def normalize(local_name: str) -> str:
            normalized_name = []
            for c in local_name:
                if c == '+':
                    break
                if c == '.':
                    continue
                normalized_name.append(c)
            return ''.join(normalized_name)


        unique_emails = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            normalized_local_name = normalize(local_name)
            normalized_email = '@'.join([normalized_local_name, domain_name])
            unique_emails.add(normalized_email)
        return len(unique_emails)
