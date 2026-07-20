# 🌻 Моя Ферма — ElIStar APK

## Что это
Android-проект для игры «Моя Ферма» от ElIStar.
Игра работает как нативное Android-приложение через WebView.

---

## 📦 Как собрать APK

### Требования
- **Android Studio** (Hedgehog 2023.1 или новее)
- **Android SDK** (API 34, минимум API 22)
- **JDK 17**

### Шаги

1. **Открыть проект**
   ```
   Android Studio → File → Open → выбрать папку /android
   ```

2. **Указать SDK путь** в `android/local.properties`:
   ```
   sdk.dir=/Users/ИМЯ/Library/Android/sdk       # macOS
   sdk.dir=C\:\\Users\\ИМЯ\\AppData\\Local\\Android\\Sdk  # Windows
   sdk.dir=/home/ИМЯ/Android/Sdk                 # Linux
   ```
   *(Android Studio предложит это сделать автоматически при открытии)*

3. **Синхронизировать Gradle**
   Android Studio → кнопка «Sync Now» в верхней панели

4. **Собрать Debug APK**
   ```
   Build → Build Bundle(s) / APK(s) → Build APK(s)
   ```
   Файл появится в: `android/app/build/outputs/apk/debug/app-debug.apk`

5. **Или через командную строку** (из папки `android/`):
   ```bash
   ./gradlew assembleDebug
   ```

### Установка на телефон
```bash
adb install android/app/build/outputs/apk/debug/app-debug.apk
```
Или перенести APK-файл на телефон и открыть (нужно разрешить установку из неизвестных источников).

---

## 🗂 Структура проекта

```
android/
├── app/
│   └── src/main/
│       ├── AndroidManifest.xml
│       ├── assets/www/
│       │   └── index.html         ← вся игра здесь
│       ├── java/pro/elistar/farmgame/
│       │   └── MainActivity.java  ← WebView обёртка
│       └── res/
│           ├── values/strings.xml
│           ├── values/styles.xml
│           └── mipmap-*/          ← иконки
├── build.gradle
├── settings.gradle
└── gradlew
```

---

## 🔧 Настройки

| Параметр | Значение |
|---|---|
| Package ID | `pro.elistar.farmgame` |
| Min Android | API 22 (Android 5.1) |
| Target | API 34 (Android 14) |
| Версия | 1.0.0 (versionCode 1) |

## 💾 Сохранения
Игра использует `localStorage` WebView — данные сохраняются локально на устройстве и не стираются при закрытии приложения.

---

*Собрано ElIStar · pro.elistar.farmgame*
