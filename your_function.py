def addProduct(products, id_barang_new, nama_barang, harga_barang):

    # this function doesn't need return value
    # modify this pass with your own implementation
    newProduct = {'id_barang': id_barang_new, 'nama_barang': nama_barang, 'harga_barang': harga_barang}
    products[id_barang_new] = newProduct

# === awal perubahan kode === #
# disini saya hanya menambahkan parameter isThrowDiskon
# parameter ini berguna jika berisi true 
# maka fungsi ini akan mereturn diskon
# jika false maka akan mereturn totalPrice
def calculateTotalPriceAfterDiscount(totalPrice, isThrowDiskon=False):
    # this function need return value
    diskon = 0
    if totalPrice >= 500000:
        diskon = totalPrice * 0.25
        totalPrice = totalPrice - diskon
    elif totalPrice >= 150000:
        diskon = totalPrice * 0.10
        totalPrice = totalPrice - diskon
    if isThrowDiskon == True:
        return diskon
    return totalPrice # modify this return with your own implementation (consider if else threshold for the discount)
