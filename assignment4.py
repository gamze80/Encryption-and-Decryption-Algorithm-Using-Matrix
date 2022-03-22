import sys
operation_type = sys.argv[1]
try:
    if operation_type == 'enc' or operation_type == 'dec':
        try:
            place = 1
            if len(sys.argv) > 5:
                raise IndexError
            f = open(sys.argv[2], 'r')
            file_name = f.name
            if file_name[-1]+file_name[-2]+file_name[-3] != 'txt':
                raise Exception
            place = 2
            if operation_type == 'enc':
                f2 = open(sys.argv[3], 'r')
                file_name = f2.name
                place = 3
                if file_name[-1]+file_name[-2]+file_name[-3] != 'txt':
                    raise Exception
                output_file = open(sys.argv[4], 'w')
                place = 4
            if operation_type == 'dec':
                my_decoding_file = open(sys.argv[3], 'r')
                file_name = my_decoding_file.name
                if file_name[-1]+file_name[-2]+file_name[-3] != 'txt':
                    raise Exception
                place = 3
                output_file = open(sys.argv[4], 'w')
                place = 4
            try:
                my_table = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
                            'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
                            'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
                            'Z': 26, ' ': 27}
                my_next_table = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: ' F', 7: 'G', 8: 'H', 9: 'I',
                                 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q',
                                 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
                                 26: 'Z', 27: ' '}
                my_matrix = []
                [my_matrix.append(i.split()) for i in f.readlines()]
                place_2 = 1
                assert my_matrix != [], AssertionError
                place_2 = 2
                my_matrix_step_1 = []
                my_matrix_values = []
                [[my_matrix_step_1.append(i.split(',')) for i in j] for j in my_matrix]
                if len(my_matrix) == 2:
                    [my_matrix_values.append(int(j[0])) for j in my_matrix_step_1]
                    [my_matrix_values.append(int(j[1])) for j in my_matrix_step_1]
                if len(my_matrix) == 3:
                    [my_matrix_values.append(int(j[0])) for j in my_matrix_step_1]
                    [my_matrix_values.append(int(j[1])) for j in my_matrix_step_1]
                    [my_matrix_values.append(int(j[2])) for j in my_matrix_step_1]
                if operation_type == 'enc':
                    encoding_file = []
                    encoding_text = []
                    [encoding_file.append(i) for i in f2.readlines()]
                    assert encoding_file != [], AssertionError
                    for i in encoding_file:
                        c = len(i)
                        k = 0
                        a = i
                        if c % len(my_matrix) == 0:
                            while k + len(my_matrix) <= len(a):
                                encoding_text.append(a[k:k+len(my_matrix)])
                                k += len(my_matrix)
                        else:
                            while len(a) % len(my_matrix) != 0:
                                a = a + ' '
                            c = len(a)
                            while k + len(my_matrix) <= len(a):
                                encoding_text.append(a[k:k+len(my_matrix)])
                                k += len(my_matrix)
                    encoding_text_number_1 = []
                    encoding_text_number_2 = []
                    for k in encoding_text:
                        for j in k:
                            if j != ' ':
                                encoding_text_number_1.append(my_table[j.upper()])
                            else:
                                encoding_text_number_1.append(my_table[j])
                        encoding_text_number_2.append(encoding_text_number_1)
                        encoding_text_number_1 = []
                    my_last_encoding_test = []
                    if len(my_matrix) == 2:
                        for i in encoding_text_number_2:
                            b = 0
                            b = i[0]*my_matrix_values[0] + i[1] * my_matrix_values[2]
                            my_last_encoding_test.append(b)
                            c = 0
                            c = i[0]*my_matrix_values[1] + i[1] * my_matrix_values[3]
                            my_last_encoding_test.append(c)
                    if len(my_matrix) == 3:
                        for i in encoding_text_number_2:
                            b = 0
                            b = i[0]*my_matrix_values[0] + i[1] * my_matrix_values[3] + i[2] * my_matrix_values[6]
                            my_last_encoding_test.append(b)
                            c = 0
                            c = i[0]*my_matrix_values[1] + i[1] * my_matrix_values[4] + i[2] * my_matrix_values[7]
                            my_last_encoding_test.append(c)
                            d = 0
                            d = i[0]*my_matrix_values[2] + i[1] * my_matrix_values[5] + i[2] * my_matrix_values[8]
                            my_last_encoding_test.append(d)
                    for i in my_last_encoding_test[0:len(my_last_encoding_test)-1]:
                        output_file.write(str(i))
                        output_file.write(',')
                    output_file.write(str(my_last_encoding_test[len(my_last_encoding_test)-1]))
                if operation_type == 'dec':
                    my_decoding_text_matrixes = []
                    my_decoding_text_matrixes_2 = []
                    my_decoding_text_matrixes= [i.split(',') for i in my_decoding_file.readlines()]
                    [[my_decoding_text_matrixes_2.append(int(i)) for i in j] for j in my_decoding_text_matrixes]
                    assert my_decoding_text_matrixes != []
                    inverse_matrix = []
                    my_decoding_text = []
                    my_decoding_text_1 = []
                    my_last_decoding_text = []
                    if len(my_matrix) == 2:
                        inverse_matrix.append((my_matrix_values[3]))
                        inverse_matrix.append(-(my_matrix_values[1]))
                        inverse_matrix.append(-(my_matrix_values[2]))
                        inverse_matrix.append((my_matrix_values[0]))
                        k = 0
                        while k + 2 <= len(my_decoding_text_matrixes_2):
                            my_decoding_text.append(my_decoding_text_matrixes_2[k:k+2])
                            k += 2
                        for i in my_decoding_text:
                            b = 0
                            b = i[0]*inverse_matrix[0] + i[1] * inverse_matrix[2]
                            my_decoding_text_1.append(b)
                            c = 0
                            c =i[0]*inverse_matrix[1] + i[1] * inverse_matrix[3]
                            my_decoding_text_1.append(c)
                        for i in my_decoding_text_1:
                            my_last_decoding_text.append(my_next_table[i])
                    if len(my_matrix) == 3:
                        my_matrix_values_step_determinant = (my_matrix_values[0] * (my_matrix_values[4] * my_matrix_values[8] - my_matrix_values[5] * my_matrix_values[7])) - (my_matrix_values[3]*(my_matrix_values[1] * my_matrix_values[8] - my_matrix_values[2] * my_matrix_values[7]))+(my_matrix_values[6] * (my_matrix_values[1] * my_matrix_values[5] - my_matrix_values[2] * my_matrix_values[4]))
                        my_inverse_matrix_kofaktor = [(my_matrix_values[4] * my_matrix_values[8] - my_matrix_values[5] * my_matrix_values[7]),
                                                     -(my_matrix_values[3] * my_matrix_values[8] - my_matrix_values[5] * my_matrix_values[6]),
                                                    (my_matrix_values[3] * my_matrix_values[7] - my_matrix_values[6] * my_matrix_values[4]),
                                                    -(my_matrix_values[1] * my_matrix_values[8] - my_matrix_values[2] * my_matrix_values[7]),
                                                    (my_matrix_values[0] * my_matrix_values[8] - my_matrix_values[2] * my_matrix_values[6]),
                                                    -(my_matrix_values[0] * my_matrix_values[7] - my_matrix_values[1] * my_matrix_values[6]),
                                                     (my_matrix_values[1] * my_matrix_values[5] - my_matrix_values[2] * my_matrix_values[4]),
                                                     -(my_matrix_values[0] * my_matrix_values[5] - my_matrix_values[2] * my_matrix_values[3]),
                                                     (my_matrix_values[4] * my_matrix_values[0] - my_matrix_values[1] * my_matrix_values[3])]
                        transpose = [my_inverse_matrix_kofaktor[0],
                                     my_inverse_matrix_kofaktor[3],
                                     my_inverse_matrix_kofaktor[6],
                                     my_inverse_matrix_kofaktor[1],
                                     my_inverse_matrix_kofaktor[4],
                                     my_inverse_matrix_kofaktor[7],
                                     my_inverse_matrix_kofaktor[2],
                                     my_inverse_matrix_kofaktor[5],
                                     my_inverse_matrix_kofaktor[8]
                                     ]
                        inverse_matrix = []
                        for i in transpose:
                            inverse_matrix.append(int(i/my_matrix_values_step_determinant))
                        k = 0
                        for i in my_decoding_text_matrixes_2:
                            while k + 3 <= len(my_decoding_text_matrixes_2):
                                my_decoding_text.append(my_decoding_text_matrixes_2[k:k+3])
                                k += 3
                        for i in my_decoding_text:
                            b = 0
                            b = i[0]*inverse_matrix[0] + i[1] * inverse_matrix[3] + i[2] * inverse_matrix[6]
                            my_decoding_text_1.append(b)
                            c = 0
                            c = i[0]*inverse_matrix[1] + i[1] * inverse_matrix[4] + i[2] * inverse_matrix[7]
                            my_decoding_text_1.append(c)
                            e = 0
                            e = i[0]*inverse_matrix[2] + i[1] * inverse_matrix[5] + i[2] * inverse_matrix[8]
                            my_decoding_text_1.append(e)
                        for i in my_decoding_text_1:
                            my_last_decoding_text.append(my_next_table[i])
                    for i in my_last_decoding_text:
                        output_file.write(i)
            except AssertionError:
                if place_2 == 1:
                    print('Key file is empty error')
                else:
                    print('Input file is empty error')
            except UnicodeDecodeError:
                print('Invalid character in input file error')
            except KeyError:
                print('Invalid character in input file error')
            except ValueError:
                print('Invalid character in key file')
        except IndexError:
            print('parameter  number error')
        except FileNotFoundError:
            if place == 1:
                print('Key file not found error')
            else:
                print('Input file not found error')
        except Exception:
            if place == 1:
                print('Key file could not be read')
            else:
                print('The input file could not be read')
        finally:
            if place == 1:
                pass
            elif place == 2:
                f.close()
            elif place == 3:
                f.close()
                if operation_type == 'enc':
                    f2.close()
                if operation_type == 'dec':
                    my_decoding_file.close()
            elif place == 4:
                f.close()
                if operation_type == 'enc':
                    f2.close()
                    output_file.close()
                if operation_type == 'dec':
                    my_decoding_file.close()
                    output_file.close()
    else:
        raise Exception
except Exception:
    print('Undefined parameter error')




