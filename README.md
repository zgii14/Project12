# TUGAS MATA KULIAH PBO (Pemrograman Berorientasi Objek) 
● Nama : Muhammad Rozagi                                                                                                                                                 
● NPM  : G1A022008                                                                                                                                                        
● Class: B  



# ● Functional programming 
Functional programming dan OOP (Object-Oriented Programming) adalah dua paradigma pemrograman yang berbeda dalam pendekatan dalam merancang dan menulis kode. Functional programming adalah paradigma pemrograman yang menekankan penggunaan fungsi sebagai unit dasar program dan menghindari perubahan state atau keadaan data. Pada paradigma ini, fungsi dianggap sebagai objek yang dapat digunakan dan dikirim sebagai argumen dalam fungsi lain, serta mengembalikan nilai sebagai hasil dari operasinya.

Di Python, fungsional programming memungkinkan penggunaan konsep seperti high-order functions, pure functions, dan lambda functions. High-order functions adalah fungsi yang dapat menerima atau mengembalikan fungsi lain sebagai argumen, atau bahkan menggunakan fungsi sebagai objek. Pure functions adalah fungsi yang hanya mengoperasikan data yang diberikan kepadanya dan tidak mengubah nilai dari data tersebut, sehingga hasil operasi fungsi selalu dapat diprediksi dengan input yang sama. Lambda functions adalah fungsi anonim atau tanpa nama yang dapat dibuat secara langsung di dalam suatu ekspresi.

Contoh penggunaan fungsional programming pada Python dapat dilihat dalam beberapa fungsi built-in seperti map(), filter(), dan reduce(). Fungsi map() dapat digunakan untuk memetakan setiap elemen dari suatu iterable ke dalam fungsi tertentu, filter() dapat digunakan untuk menyaring elemen dari iterable berdasarkan kondisi yang diberikan, dan reduce() dapat digunakan untuk menggabungkan semua elemen dari iterable ke dalam satu nilai.
Sebagai contoh perbedaan fungsi yang termasuk ke dalam pemrograman fungsional dan bukan diimplementasikan dalam bahasa pemrograman Python sebagai berikut:

```a = 0
def increment(a):
    return a + 1
```
`Pada kode tersebut, terdapat variabel a yang memiliki nilai awal 0 dan sebuah fungsi increment() yang menerima sebuah argumen a dan akan mengembalikan nilai dari a ditambah dengan 1 . Fungsi increment() tidak mengubah nilai variabel a secara langsung, tetapi mengambil nilai variabel a sebagai argumen dan menghasilkan nilai yang baru. Dalam konsep functional programming, perubahan state seperti ini harus dihindari, dan penggunaan argumen fungsi harus diperhatikan secara cermat.
Selain itu, fungsi increment() bersifat "pure", artinya fungsi ini tidak memiliki efek samping yang memengaruhi lingkungan di luar fungsi. Hal ini penting dalam konsep functional programming untuk memudahkan pengujian dan meminimalkan efek samping pada program.`

Penerapan paradigma fungsional programming pada Python dapat membantu memudahkan pengembangan program yang bersifat parallel, mudah untuk dibaca, mudah untuk diuji, serta dapat meningkatkan performa program jika dilakukan dengan benar.

# ● Object Oriented Programming (OOP)
Pemrograman berorientasi objek, atau hanya disebut sebagai "OOP", adalah model pemrograman perangkat lunak berdasarkan konsep objek, bukan hanya fungsi dan prosedur. OOP dirancang sedemikian rupa sehingga konsep dunia nyata dapat diprogram dalam program komputer. Seperti namanya, OOP menggunakan objek dalam pemrograman yang diatur ke dalam kelas, yang memungkinkan objek individu untuk dikelompokkan bersama. Setiap objek dalam OOP bertanggung jawab untuk serangkaian tugas. Jadi, berbagai tugas dalam program dilakukan, dengan menjalankan operasi yang didefinisikan pada objek yang sesuai. Meskipun, fitur dasar dari OOP ditemukan pada tahun 1960-an, baru pada tahun 1980-an bahasa berorientasi objek mulai mendapatkan perhatian. OOP adalah ide revolusioner dan ada sejumlah alasan mengapa ia menjadi paradigma pemrograman yang dominan dalam beberapa dekade terakhir. 
OOP (Object-Oriented Programming) atau Pemrograman Berorientasi Objek adalah paradigma pemrograman yang berfokus pada konsep objek yang dapat diidentifikasi, memiliki sifat dan perilaku yang dapat didefinisikan, serta dapat berinteraksi dengan objek lain. OOP digunakan untuk memodelkan masalah dunia nyata dan memungkinkan untuk membuat program yang lebih kompleks dan mudah dimengerti. Python merupakan bahasa pemrograman yang mendukung OOP dan memiliki fitur-fitur berikut:

➤Class  
Class adalah blueprint atau cetakan dari suatu objek. Class dapat digunakan untuk membuat banyak objek dengan sifat dan perilaku yang sama. Suatu class      memiliki atribut (variabel) dan metode (fungsi) yang dapat digunakan untuk mengakses dan memanipulasi objek dari class tersebut._  

➤Encapsulation  
Encapsulation atau pengkapsulan adalah teknik OOP untuk menyembunyikan detail implementasi dari pengguna dan memungkinkan pengguna untuk mengakses objek hanya melalui metode yang disediakan oleh class. Hal ini dapat meningkatkan keamanan dan kesalahan yang mungkin terjadi pada program. Dalam Python, pengkapsulan dapat dilakukan dengan menandai atribut dan metode sebagai private menggunakan awalan karakter garis bawah ("_"). Perlu di ingat, cara ini tidak sepenuhnya membuat suatu atribut bersifat private, tetapi lebih sebagai pengingat dan best practice saja.

➤Inheritance  
Inheritance atau pewarisan adalah teknik OOP untuk menurunkan sifat dan perilaku dari satu class ke class lain. Class yang diturunkan disebut subclass atau anak class, sedangkan class yang mewariskan disebut superclass atau induk class. Dalam Python, pewarisan dapat dilakukan dengan menuliskan nama superclass dalam tanda kurung setelah nama subclass. Contoh Employee(Person) artinya kelas Employee mewarisi dari kelas Person.  

➤Polymorphism  
Polymorphism atau banyak bentuk adalah kemampuan suatu objek untuk memiliki banyak bentuk atau perilaku yang berbeda-beda dalam situasi yang berbeda. Polymorphism dapat dicapai melalui inheritance dan metode overriding atau overloading.

➤Abstraction (Abstraksi)  
Konsep abstraksi memungkinkan untuk memfokuskan pada fitur penting dari suatu objek dan mengabaikan detail implementasi yang tidak penting.  
Berikut untuk penerapan OOP pada python : https://github.com/zgii14/Project12/blob/04d8ec67ea942d72cdb4537144d732f39aac2322/oop-Program.py
# ● Perbedaan Functional Programming & Object Oriented Programming
Perbedaan antara OOP dan functional programming di Python dapat dijelaskan sebagai berikut:  

**Pendekatan Konsep**  
OOP adalah pendekatan untuk membangun program dengan fokus pada objek, sedangkan functional programming adalah pendekatan untuk membangun program dengan fokus pada fungsi.

**Pembagian Tugas**  
Dalam OOP, tugas dibagi ke dalam kelas atau objek yang terpisah dan berinteraksi satu sama lain melalui metode. Dalam functional programming, tugas dibagi menjadi fungsi-fungsi yang saling berhubungan dan saling berinteraksi.

**State**  
OOP memiliki konsep state, di mana setiap objek dapat memiliki atribut dan nilai yang berbeda. Fungsi-fungsi dalam OOP dapat memanipulasi state objek. Sedangkan, dalam functional programming, fungsi tidak memanipulasi state, dan hasilnya hanya tergantung pada parameter masukan.

**Perubahan Data**  
OOP mendorong perubahan data yang dilakukan melalui objek atau kelas, sementara functional programming mendorong penggunaan fungsi-fungsi yang tidak mengubah nilai dari variabel masukan.

**Keterbacaan Kode**  
OOP cenderung lebih mudah dibaca dan dimengerti oleh programmer yang sudah terbiasa dengan paradigma pemrograman objek. Sementara functional programming cenderung lebih sulit dipahami bagi programmer yang tidak terbiasa dengan konsep pemrograman fungsional.
Pemilihan paradigma pemrograman tergantung pada kebutuhan proyek dan preferensi programmer. OOP lebih cocok untuk proyek besar yang kompleks dan memerlukan manajemen state yang rumit, sedangkan functional programming lebih cocok untuk pemrosesan data paralel dan algoritma matematis.
