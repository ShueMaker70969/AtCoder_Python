def manacher_end(s):
    # Transform the string to avoid even-length palindrome issues
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n  # Array to store palindrome radius
    c = 0  # Center of the palindrome
    r = 0  # Right boundary of the palindrome

    for i in range(n):
        mirror = 2 * c - i  # Mirror position of i around center c

        if i < r:
            p[i] = min(r - i, p[mirror])

        # Expand around center i
        while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        # Update center and right boundary if expanded beyond r
        if i + p[i] > r:
            c = i
            r = i + p[i]

    # Find the longest palindrome that ends at the last character of the original string
    max_length = 0
    center_index = 0
    for i in range(n):
        if (i + p[i] == n - 1) and p[i] > max_length:  # Ensure palindrome reaches the end
            max_length = p[i]
            center_index = i

    # Extract the longest palindromic substring at the end of the original string
    if max_length == 0:
        return ""  # No valid palindrome found at the end

    start = (center_index - max_length) // 2  # Convert back to original index
    return s[start:start + max_length]

# Example usage:
str = input()
palin = manacher_end(str)
str = str.replace(palin,'')
print(str+palin+str[::-1])
