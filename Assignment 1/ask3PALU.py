import numpy as np


# Λύνω το γραμμικό σύστημα Lx = b όπου ο πίνακας L είναι κάτω τριγωνικός
def forward_substitution(L, b):
    m = len(b)
    x = np.empty(m)

    for v in range(m):
        if L[v][v] == 0:
            # η τιμή στην διαγώνιο είναι μηδέν
            x[v] = 0
            # η τιμή της τρέχουσας μεταβλητής είναι αδιάφορη
            continue
        # υπολογίζω την τιμή της v-ιοστής μεταβλητής
        value = b[v]
        # αφαιρώ τις τιμές των μεταβλητών που ήδη γνωρίζω
        # στην κάτω αριστερά γωνία του πίνακα
        for i in range(v):
            value -= L[v][i] * x[i]
        # διαιρώ με τον συνελεστή της v-ιοστής μεταβλητής για να πάρω την τελική τιμή της
        value /= L[v][v]
        # αποθηκεύω την τιμή της v-ιοστής μεταβλητής
        x[v] = value

    return x


# Λύνω το γραμμικό σύστημα Ux = b όπου ο πίνακας U είναι άνω τριγωνικός
def backward_substitution(U, b):
    m = len(b)
    x = np.empty(m)

    for v in range(m - 1, -1, -1):
        if U[v][v] == 0:
            # η τιμή στην διαγώνιο είναι μηδέν
            x[v] = 0
            continue
        # υπολογίζω την τιμή v-ιοστής μεταβλητής
        value = b[v]
        # αφαιρώ τις τιμές των μεταβλητών που ήδη γνωρίζω
        # στην πάνω δεξιά γωνία του πίνακα
        for i in range(v + 1, m, 1):
            value -= U[v][i] * x[i]
        # διαιρώ με τον συνελεστή της v-ιοστής μεταβλητής για να πάρω την τελική τιμή της
        value /= U[v][v]
        # αποθηκεύω την τιμή της v-ιοστής μεταβλητής
        x[v] = value

    return x


def palu(A):
    m = len(A)

    P = np.identity(m)  # δημιουργώ μοναδιαίο πίνακα μεγέθους m
    L = np.identity(m)  # δημιουργώ μοναδιαίο πίνακα μεγέθους m

    for x in range(m):

        pivotRow = x

        '''
        if A[pivotRow][x] == 0:
            # search for a non-zero pivot
            for y in range(x + 1, m, 1):
                if A[y][x] != 0:
                    pivotRow = y
                    break
        '''

        # ψάχνω το καλύτερο pivot
        for y in range(x + 1, m, 1):
            if abs(A[y][x]) > abs(A[pivotRow][x]):
                pivotRow = y

        if A[pivotRow][x] == 0:
            # δεν βρήκαμε καμία γραμμή με οδηγό συντελεστή διάφορο του μηδενός
            # αυτό σημαίνει ότι ο πίνακας έχει μόνο μηδενικά σε αυτή τη στήλη
            # οπότε δεν χρειάζεται να ψάξουμε για pivots στην τρέχουσα στήλη x
            continue

        # χρησιμοποίησαμε pivot που δεν είναι στη διαγώνιο;
        if pivotRow != x:
            # οπότε πρέπει να κάνουμε swap τον μέρος της γραμμής pivot μετά το x συμπεριλαμβανομένου και του x
            # με το ίδιο δεξί μέρος της γραμμής του x όπου αναμέναμε το pivot
            for i in range(x, m, 1):
                # swap the two values columnwise
                (A[x][i], A[pivotRow][i]) = (A[pivotRow][i], A[x][i])

            # πρέπει να αποθηκεύσουμε το ότι κάναμε swap στον πίνακα P
            P[[x, pivotRow]] = P[[pivotRow, x]]  # swap την γραμμή pivot με τη γραμμή x

            # we also need to swap the rows in the L matrix
            # however, the relevant part of the L matrix is only the bottom-left corner
            # and before x

            # πρέπει επίσης να κάνουμε swap τις γραμμές του πίνακα L
            # ωστόσο, το μέρος που μας ενδιαφέρει από τον πίνακα L έιναι μόνο η κάρω αριστερά γωνία
            # και πριν το x
            for i in range(x):
                (L[x][i], L[pivotRow][i]) = (L[pivotRow][i], L[x][i])

        # τώρα η γραμμή pivot είναι η x
        # ψάχνουμε για τις γραμμές όπου ο οδηγός συντελεστής πρέπει να μηδενιστεί
        for y in range(x + 1, m, 1):
            currentValue = A[y][x]
            if currentValue == 0:
                # variable already eliminated, nothing to do
                # η μεταβλητή έχει ήδη μηδενιστεί, δεν χρειάζεται να κάνουμε κάτι
                continue

            pivot = A[x][x]

            pivotFactor = currentValue / pivot

            # αφαιρούμε την γραμμή pivot από την τρέχουσα γραμμή
            A[y][x] = 0
            for i in range(x + 1, m, 1):
                A[y][i] -= pivotFactor * A[x][i]

            # write the pivot factor to the L matrix
            # αποθηκεύουμε τον παράγοντα pivot στον πίνακα L
            L[y][x] = pivotFactor

        # το pivot πρέπει να είναι στην σωστή θέση αν βρήκαμε τουλάχιστον έναν
        # οδηγό συντελεστή διάφορο του μηδενός στην τρέχουσα στήλη x
        assert A[x][x] != 0
        for y in range(x + 1, m, 1):
            assert A[y][x] == 0

    return P, L, A


def plu_solve(A, b):
    P, L, U = palu(A)

    print('P =')
    print(P)
    print('A =')
    print(A)
    print('L =')
    print(L)
    print('U =')
    print(U)

    # πολλαπλασιάζω τον πίνακα P με το διάνυσμα b
    b = np.matmul(P, b)

    y = forward_substitution(L, b)
    x = backward_substitution(U, y)

    return x


A = [[2, 1, 5], [4, 4, -4], [1, 3, 1]]
A = np.array(A)

b = [5, 0, 6]
b = np.array(b)

x = plu_solve(A, b)

print('x =', x)
