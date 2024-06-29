# Case I : Video Streaming Services
## PacFlix adalah platform video streaming
-- PacFlix memiliki 3 plan: 
    - Basic Plan
    - Standard Plan
    - Premium Plan
-- dimana masing masing plan memiliki benefitnya seperti di tabel dibawah ini:
## Table Plan
| **Basic Plan**       | **Standard Plan**                                       | **Premium Plan**                                               | **Services**   |
|----------------------|---------------------------------------------------------|----------------------------------------------------------------|----------------|
| ✓                    | ✓                                                       | ✓                                                              | can_stream     |
| ✓                    | ✓                                                       | ✓                                                              | can_download   |
| ✓                    | ✓                                                       | ✓                                                              | has_SD         |
|                      | ✓                                                       | ✓                                                              | has_HD         |
|                      |                                                         | ✓                                                              | has_UHD        |
| 1                    | 2                                                       | 4                                                              | num_of_devices |
| 3rd party movie only | Basic Plan Content + Sports  (F1, Football, Basketball) | Basic Plan + Standard Plan +  PacFlix Original Series or Movie | content        |
| Rp 120.000,-         | Rp 160.000,-                                            | Rp 200.000,-                                                   | price          |

## Problem & Objective
Membuat simpel program dari PacFlix & user bisa menggunakan fitur-fitur yang tersedia seperti: mengecek layanan plan yang tersedia, mengetahui plan yang saat ini digunakan, perubahan plan/upgread, dan pendaftaran new plan bagi user baru apabila mendapatkan referal code bisa mendapatkan potongan harga & sebaliknya harga normal.
Input data yang tersedia:
- User Name
- Active Plan
- Duration Plan
- Referral Code

## Requirment yang dibutuhkan
- [ ] `check_benefit()` --> tampilkan semua benefit
- [ ] `check_plan(username)` --> tampilkan benefit yang didapatkan dan udah langganan berapa lama (done)
- [ ] `upgrade_plan(username, current_plan, new_plan)` --> harga final, if langganan > 12 bulan akan dapet diskon 5% 
- [ ] `pick_plan(new_plan, code_referral)` --> untuk new user, harga final kalo pake kode referral dapet diskon 4%

## Validasi Program (Tes Run Program)
- user1 = User(username "Bagus")
- Check_plan()
- Check_benefit()
- Upgread_plan()

- NewUser = faizal
- pick_plan()
- regenerate_referral_code()
- total_price with referral code
- total_price with (none/"") referral code
- total_price with referral code doesnt exist in the data