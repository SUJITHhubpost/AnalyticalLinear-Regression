import sum_of_squares as ssy
import reg_functions as r




# Take inputs
if __name__ == "__main__":
    
    # X, Y = inputs()

    X = [1.00, 2.00, 3.00, 4.00, 5.00]
    Y = [1.00, 2.00, 1.30, 3.75, 2.25]

    Mx, My = r.mean(X, Y)

    sx = r.std_deviation(X)
    sy = r.std_deviation(Y)

    x, y, corr = r.corr(X, Y)

    r = corr


    b = r*(sy/sx)
    A = My - (b * Mx)

    print("Mx = {} ,My = {} ,sx = {}, sy = {}, r = {}\n".format(Mx, My, sx, sy, r))

    r.Regression_line(X, Y, b, A)