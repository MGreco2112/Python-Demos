if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    new_tuple = tuple(integer_list)
    h_tuple = hash(new_tuple)
    print(h_tuple)