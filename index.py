from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
driver.maximize_window()


driver.get("https://www.viajesexito.com/")
paquetes = driver.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[2]/a')
time.sleep(2)
paquetes.click();
time.sleep(2)

vueloHotel = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div/div/ul/li[1]/label')
time.sleep(2)
vueloHotel.click();
time.sleep(2);

ciudadOrigen = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div/div/input')
time.sleep(2)
textoCiudadOrigen= "Bogotá, Colombia (BOG)"

ciudadOrigen.click();
ciudadOrigen.send_keys(textoCiudadOrigen);


ciudadDestino=driver.find_element(by=By.NAME,value="CityPredictiveTo_netactica_airhotel");
time.sleep(2)
textoCiudadDestino= "Punta Cana, Republica Dominicana (PUJ)"

ciudadDestino.click();
ciudadDestino.send_keys(textoCiudadDestino);
time.sleep(2);

saliendo=driver.find_element(by=By.NAME,value="DateFrom_netactica_airhotel");
time.sleep(2)
saliendo.click();
time.sleep(2);

botonDiaSalida=driver.find_element(By.XPATH,"/html/body/div[21]/div[1]/table/tbody/tr[3]/td[3]/a");
time.sleep(2)
botonDiaSalida.click();
time.sleep(2);

botonDiaRegreso=driver.find_element(By.XPATH,"/html/body/div[21]/div[1]/table/tbody/tr[4]/td[4]/a");
time.sleep(2)
botonDiaRegreso.click();
time.sleep(2);

botonHabitacion=driver.find_element(By.XPATH,"/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div/p");
time.sleep(2)
botonHabitacion.click();
time.sleep(2);

botonAumentarHabitacion=driver.find_element(By.XPATH,"/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div/span[2]/button/span");
time.sleep(2)
botonAumentarHabitacion.click();
time.sleep(2);


aplicar=driver.find_element(By.XPATH,"/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/button");
time.sleep(2)
aplicar.click();
time.sleep(2);


buscar=driver.find_element(By.XPATH,"/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[4]/a/span");
time.sleep(2)
buscar.click();
time.sleep(20);

print("----------------------------PRECIO-DE-LOS-VUELOS--------------------------------/")
for i in range(2, 5, 1):
    for j in range(1, 6, 1):
        precioVuelo=driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div["+str(j)+"]/div["+str(i)+"]").text;
        if(precioVuelo!=" "):
            print(precioVuelo)

        
print("--------------------------------------------------------------")
time.sleep(2);

opcionesAvanzadas = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
Aerolinea="Avianca (AV)";
opcionesAvanzadas.send_keys(Aerolinea);
time.sleep(2)


botonAerolinea=driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input");
time.sleep(2)
botonAerolinea.click();
time.sleep(16);


driver.quit()






