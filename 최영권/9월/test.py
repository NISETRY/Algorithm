def caesar_encrypt(plaintext: str, shift: int) -> str:
    """
    입력: 알파벳 대문자 문자열
    shift: 밀어낼 칸 수 (양수 = 오른쪽, 음수 = 왼쪽)
    """
    result = []
    s = shift % 26
    for ch in plaintext:
        new_code = (ord(ch) - ord('A') + s) % 26 + ord('A')
        result.append(chr(new_code))
    print(result)
    return ''.join(result)

print(caesar_encrypt('SRKKCVJJRWP', 9))