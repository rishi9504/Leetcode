class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]

        length_diff = len(num1) - len(num2)

        if length_diff < 0:

            num1 += "0" * -length_diff

        else:

            num2 += "0" * length_diff

        result, carry = [], 0

        for d1, d2 in zip(num1, num2):

            carry, digit = divmod(int(d1) + int(d2) + carry, 10)

            result.append(str(digit))

        if carry:

            result.append(str(carry))

        return "".join(result[::-1])
        
