from scipy.stats import norm #funkcje do obliczeń numerycznych, alegabraicznych, uczenia maszynowego, metody do rozwiązywania równań różniczkowych
from csv import writer
import numpy as np
#przy użyciu funkcji norm tworzy się obiekty, reprezentujące rozkłady prawdopodobieństwa, każdy z rozkładów parametryzowany jest średnią i odchyleniem standardowym
#loc - średnia, scale - odchylenie standardowe

def generate_horizontal_points(num_points: int = 2000, width: float = 100, length: float = 100):
    #Ustawienie ograniczeń dla generowanych współrzędnych x i y
    x_min, x_max = -width / 2, width / 2
    y_min, y_max = -length / 2, length / 2

    #Rozkłady normalne dla współrzędnych x,y,z
    distribution_x = norm(loc=0, scale=width / 4) #Skala może być dostosowana do wielkości obszaru
    distribution_y = norm(loc=0, scale=length / 4)
    distribution_z = norm(loc=0.2, scale=0.05)

    #Generacja punktów
    x = []
    y = []
    z = []

    while len(x) < num_points:
        point_x = distribution_x.rvs(size=1)[0]
        point_y = distribution_y.rvs(size=1)[0]

        #Sprawdzenie,czy punkt jest w obszarze ograniczonym
        if x_min <= point_x <= x_max and y_min <= point_y <= y_max:
            x.append(point_x)
            y.append(point_y)
            z.append(distribution_z.rvs(size=1)[0])

    points = zip(x, y, z)
    return points

def generate_vertical_points(num_points: int = 2000, width: float = 100, height: float = 100):
    #Ustawienie ograniczeń dla generowanych współrzędnych x i y
    x_min, x_max = -width / 2, width / 2
    y_min, y_max = -width / 2, width / 2
    z_min, z_max = 0, height #Ograniczenie wysokości

    #Rozkłady normalne dla współrzędnych x i y
    distribution_x = norm(loc=0, scale=width / 4) #Skala może być dostosowana do wielkości obszaru
    distribution_y = norm(loc=0, scale=width / 4)

    #Generacja punktów
    x = []
    y = []
    z = []

    while len(x) < num_points:
        point_x = distribution_x.rvs(size=1)[0]
        point_y = distribution_y.rvs(size=1)[0]

        #Sprawdzenie, czy punkt znajduje się w obszarze ograniczonym
        if x_min <= point_x <= x_max and y_min <= point_y <= y_max:
            x.append(point_x)
            y.append(0) #Ustawienie wartości dla osi y jako 0
            z.append(np.random.uniform(z_min, z_max))  #Losowanie z zakresu [z_min, z_max]

    points = zip(x, y, z)
    return points

def generate_cylindrical_points(num_points: int = 2000, radius: float = 50, height: float = 100):
    #Generowanie losowych wartości kąta
    theta_values = np.random.uniform(0, 2 * np.pi, num_points)

    #Wartości promienia ustawione na stały promień
    r_values = np.full(num_points, radius)

    #Losowe wartości wysokości wzdłuż osi z
    z_values = np.random.uniform(0, height, num_points)

    #Konwersja współrzędnych cylindrycznych na kartezjańskie
    x = r_values * np.cos(theta_values) #r_values - promień, cos(theta_values) - kąt
    y = r_values * np.sin(theta_values)

    points = zip(x, y, z_values)
    return points

if __name__ == '__main__': #dzięki temu tylko górny kod się wykona, ta część nie
    cloud_point_horizontal = generate_horizontal_points(2000)
    with open('powierzchnia_pozioma.xyz', 'w', encoding='utf-8', newline='\n') as csvfile: #otwiera plik do zapisu
        csvwriter = writer(csvfile)
        for d in cloud_point_horizontal:
            csvwriter.writerow(d)

    cloud_point_vertical = generate_vertical_points(2000)
    with open('powierzchnia_pionowa.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:  # otwiera plik do zapisu
        csvwriter = writer(csvfile)
        for d in cloud_point_vertical:
            csvwriter.writerow(d)

    cloud_point_cylindrical = generate_cylindrical_points(2000)
    with open('powierzchnia_cylindryczna.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:  # otwiera plik do zapisu
        csvwriter = writer(csvfile)
        for d in cloud_point_cylindrical:
            csvwriter.writerow(d)