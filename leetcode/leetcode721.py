class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        email_to_id = {}
        email_to_name = {}

        id = 0

        for account in accounts:
            name = account[0]

            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = id
                    email_to_name[email] = name
                    id += 1

        parent = list(range(id))
        size = [1] * id

        def find(x):
            if parent[x] == x:
                return x

            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return

            if size[root_x] < size[root_y]:
                root_x, root_y = root_y, root_x

            parent[root_y] = root_x
            size[root_x] += size[root_y]

        for account in accounts:
            first_email = account[1]

            for email in account[2:]:
                union(
                    email_to_id[first_email],
                    email_to_id[email]
                )

        groups = {}

        for email in email_to_id:
            email_id = email_to_id[email]
            root = find(email_id)

            if root not in groups:
                groups[root] = []

            groups[root].append(email)

        result = []

        for emails in groups.values():
            emails.sort()

            name = email_to_name[emails[0]]

            result.append([name] + emails)

        return result


accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnnybravo@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com", "john_newyork@mail.com"],
    ["Mary", "mary2@mail.com"],
    ["David", "david@mail.com"],
    ["Mary", "mary@mail.com", "mary.work@mail.com"]
]

solution = Solution()

print(solution.accountsMerge(accounts))