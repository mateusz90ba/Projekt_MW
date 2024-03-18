from scipy.stats import norm #funkcje do obliczeń numerycznych, alegabraicznych, uczenia maszynowego, metody do rozwiązywania równań różniczkowych
from csv import writer

#przy użyciu funkcji norm tworzy się obiekty, reprezentujące rozkłady prawdopodobieństwa, każdy z rozkładów parametryzowany jest średnią i odchyleniem standardowym
#loc - średnia, scale - odchylenie standardowe

def generate_pointss(num_points: int = 2000):
    distribution_x = norm(loc = 0, scale = 20) #jeżeli loc = 0, to lidar jest umieszczony w początku układu współrzędnych
    distribution_y = norm(loc = 0, scale = 200) #scale tu większe oznacza, że punkty będą bardziej rozciągnięte, a w "x" skupione (gęste)
    distribution_z = norm(loc = 0.2, scale = 0.05) #loc inne oznacza, że przy powierzchni będzie, jak w autonomicznym pojeździe ? - film 13

    #z rozkładów prawdopodobieństwa powyżej będą losowane punkty, czyli zmienne losowe
    num_points = 2000
    x = distribution_x.rvs(size = num_points) #rvs - randiom variable sample, size - rozmiar próbki
    y = distribution_y.rvs(size = num_points)
    z = distribution_z.rvs(size = num_points)

    points = zip(x,y,z) #powstaje lista krotek, które będą zawierały współrzędne x, y i z
    return points

if __name__ == '__main__': #dzięki temu tylko górny kod się wykona, ta część nie
    cloud_point = generate_pointss(2000)
    with open('LidarData.xyz', 'w', encoding='utf-8', newline='\n') as csvfile: #otwiera plik do zapisu
        csvwriter = writer(csvfile)
        for d in cloud_point:
            csvwriter.writerow(d)