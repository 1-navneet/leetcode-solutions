class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        sume = 0
        for i in range(len(accounts)):
            if sum(accounts[i]) > sume:
                sume = sum(accounts[i])
        return sume
