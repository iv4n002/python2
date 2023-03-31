def esta_ordenada(nums):
    """
    Determina si la llista de nombres donada està ordenada en ordre ascendent, descendent o no està ordenada.
    """
    if all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):
        return "està ordenada de forma ascendent"
    elif all(nums[i] >= nums[i+1] for i in range(len(nums)-1)):
        return "està ordenada de forma descendent"
    else:
        return "no està ordenada"


def main():
    nums_str = input("Introdueix la llista de nombres separats per espais: ")
    nums = list(map(int, nums_str.split()))
    print(f"La llista {nums} {esta_ordenada(nums)}")


if __name__ == "__main__":
    main()
