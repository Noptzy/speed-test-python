import speedtest

def speed_test():
    try:
        st = speedtest.Speedtest()
        print("Mengetes Kecepatan...")
         # Mencoba Tes Kecepatan Download
        download_speed = st.download() / 1000000  # Ubah Ke Mbps

        # Mencoba Tes Kecepatan Upload
        upload_speed = st.upload() / 1000000  # Ubah Ke Mbps

        # Print Hasil
        print("Download Speed: {:.2f} Mbps".format(download_speed))
        print("Upload Speed: {:.2f} Mbps".format(upload_speed))
    except speedtest.SpeedtestException as e:
        print("Error, tidak terhubung ke internet")
        
speed_test()