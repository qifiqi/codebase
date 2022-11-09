from Crypto.Cipher import AES

password = b'aaad3e4fd540b0f79dca95606e72bf93' #秘钥，b就是表示为bytes类型
text = b'pX7rCko1ZPLJXbyU3qjcDqAp042BK5yCrhhNlUZEBd6lHKILemhbvHD1YkhQ7FDbOO67LXHsECLhREpE4EgC33ovLqy1dbR8KcUTJs_JYGnTdumkV_DRl_Om8A1NRl-ziFO-iM0ZddbzKSkJTRyhMarY16ETj2Cmyt7b_uEhzFboosmFoWaKYfBkWl6qcuwyo6wr9HXI4UJsDNluzkCyC2_pp9Vb9GgSgezuKF1AZhPrCa_wPgeGpJla18lz1qAQtP6eGFcy_vbtX12RA5mgSTwUeNYZMKGk90s7icmJF38' #需要加密的内容，bytes类型
aes = AES.new(password,AES.MODE_ECB) #创建一个aes对象
# AES.MODE_ECB 表示模式是ECB模式
den_text = aes.decrypt(text) # 解密密文
print("明文：",den_text)
