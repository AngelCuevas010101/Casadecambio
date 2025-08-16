# 🏦 Casa de Cambio MXN ↔ USD

Una aplicación moderna y elegante para convertir entre **Pesos Mexicanos (MXN)** y **Dólares Estadounidenses (USD)** con tipos de cambio en tiempo real.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Kivy](https://img.shields.io/badge/Kivy-2.1.0+-orange.svg)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Android-lightgrey.svg)

## 🌟 Características

### ✨ **Interfaz Moderna**
- 🎨 Diseño elegante con tema oscuro
- 📱 Responsive y fácil de usar
- 🖼️ Iconos y emojis para mejor UX
- 🌈 Colores vibrantes y profesionales

### 💱 **Conversión Inteligente**
- 🔄 **Conversión bidireccional** (MXN ↔ USD)
- ⚡ **Tiempo real**: Convierte mientras escribes
- 🌐 **API en vivo**: Tipos de cambio actualizados
- 🎯 **Precisión**: Hasta 2 decimales

### 🔧 **Funcionalidades Avanzadas**
- 📊 Actualización automática de tipos de cambio
- 🛡️ Validación robusta de entrada de datos
- ⚠️ Manejo inteligente de errores
- 📱 Optimizado para múltiples plataformas

## 📸 Capturas de Pantalla

### Versión Desktop (CustomTkinter)
```
🏦 Casa de Cambio
Pesos Mexicanos ↔ Dólares Estadounidenses

┌─────────────────────────────────────┐
│        Tipo de Cambio Actual        │
│       1 USD = $17.85 MXN            │
│    Última actualización: 14:32:15   │
│    [Actualizar Tipo de Cambio]      │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│           Conversión                │
│   Tipo: [MXN a USD ▼]               │
│   Cantidad: [1000.00]               │
│                                     │
│                                     │
│   Resultado: $56.02 USD             │
└─────────────────────────────────────┘
```

### Versión Móvil (Kivy)
- Interfaz táctil optimizada
- Scroll suave para dispositivos pequeños
- Botones grandes para fácil navegación

## 🚀 Instalación Rápida

### Prerrequisitos
- Python 3.8 o superior
- Conexión a internet (para tipos de cambio)

### Windows
```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/casa-cambio-mxn-usd.git
cd casa-cambio-mxn-usd

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar versión desktop
python casa_cambio_desktop.py

# O versión móvil/multiplataforma
python casa_cambio_mobile.py
```

### Linux/macOS
```bash
# Clonar e instalar
git clone https://github.com/tu-usuario/casa-cambio-mxn-usd.git
cd casa-cambio-mxn-usd
pip3 install -r requirements.txt

# Ejecutar
python3 casa_cambio_desktop.py
```

## 📱 Compilar para Android

### Usando Buildozer (Recomendado)
```bash
# Instalar buildozer
pip install buildozer

# Compilar APK de prueba
buildozer android debug

# APK para producción
buildozer android release
```

### Requisitos para Android
- Linux (Ubuntu 20.04+ recomendado)
- Java JDK 8
- Android SDK
- 4GB RAM mínimo para compilación

## 📦 Crear Ejecutable Windows

```bash
# Instalar PyInstaller
pip install pyinstaller

# Crear ejecutable
pyinstaller --onefile --windowed --name="CasaDeCambio" casa_cambio_desktop.py

# Ejecutable en carpeta "dist/"
```

## 🛠️ Tecnologías Utilizadas

### Desktop Version
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)**: Interfaz moderna para desktop
- **[Requests](https://requests.readthedocs.io/)**: Cliente HTTP para APIs
- **[Threading](https://docs.python.org/3/library/threading.html)**: Operaciones asíncronas

### Mobile Version
- **[Kivy](https://kivy.org/)**: Framework multiplataforma
- **[Buildozer](https://buildozer.readthedocs.io/)**: Empaquetado para Android/iOS
- **[Clock](https://kivy.org/doc/stable/api-kivy.clock.html)**: Programación de tareas

### API de Tipos de Cambio
- **[ExchangeRate-API](https://exchangerate-api.com/)**: Tipos de cambio gratuitos y confiables

## 🎯 Casos de Uso

### 🏪 **Comercio**
- Tiendas fronterizas
- Casas de cambio
- Comercio en línea

### 🧑‍💼 **Personal**
- Viajeros a EE.UU./México
- Freelancers internacionales
- Inversores en divisas

### 🎓 **Educativo**
- Enseñanza de matemáticas financieras
- Proyectos escolares
- Aprendizaje de programación

## 📊 Funcionalidades Técnicas

| Característica | Desktop | Móvil | Descripción |
|----------------|---------|--------|-------------|
| Tipos de cambio en vivo | ✅ | ✅ | API actualizada cada minuto |
| Conversión bidireccional | ✅ | ✅ | MXN→USD y USD→MXN |
| Validación de entrada | ✅ | ✅ | Solo números válidos |
| Manejo de errores | ✅ | ✅ | Conexión e input inválido |
| Tema oscuro | ✅ | ✅ | Interfaz moderna |
| Responsive design | ✅ | ✅ | Adaptable a pantalla |

## 🔄 Próximas Actualizaciones

### v2.0 (Planeado)
- [ ] 📊 Historial de conversiones
- [ ] 💾 Guardado automático de preferencias
- [ ] 🌍 Soporte para más monedas (EUR, CAD, JPY)
- [ ] 📈 Gráficos de tendencia del tipo de cambio
- [ ] 🔔 Notificaciones de cambios significativos
- [ ] 🌐 Modo sin conexión con último tipo conocido

### v2.1 (Futuro)
- [ ] 🎨 Temas personalizables (claro/oscuro/auto)
- [ ] 🏢 Calculadora de comisiones bancarias
- [ ] 📱 Widget para escritorio
- [ ] 🔐 Cifrado de datos sensibles
- [ ] 📧 Exportar historial a Excel/PDF

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor:

1. 🍴 Fork el proyecto
2. 🌿 Crea tu rama (`git checkout -b feature/nueva-caracteristica`)
3. 💾 Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. 📤 Push a la rama (`git push origin feature/nueva-caracteristica`)
5. 🔄 Abre un Pull Request

### 🐛 Reportar Bugs
- Usa la pestaña **Issues**
- Describe el problema detalladamente
- Incluye capturas de pantalla si es posible
- Menciona tu sistema operativo

### ✨ Solicitar Características
- Abre un **Issue** con la etiqueta `enhancement`
- Explica por qué sería útil
- Proporciona ejemplos de uso

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT** - ver el archivo [LICENSE](LICENSE) para detalles.

```
MIT License

Copyright (c) 2025 [Tu Nombre]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

## 👨‍💻 Autor
Angel Cuevas

## 🙏 Agradecimientos

- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** por la librería de UI moderna
- **[Kivy Team](https://kivy.org/)** por el framework multiplataforma
- **[ExchangeRate-API](https://exchangerate-api.com/)** por los datos de tipos de cambio
- **Comunidad de Python** por las herramientas y documentación

## 📈 Estadísticas del Proyecto

![GitHub repo size](https://img.shields.io/github/repo-size/tu-usuario/casa-cambio-mxn-usd)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/tu-usuario/casa-cambio-mxn-usd)
![GitHub top language](https://img.shields.io/github/languages/top/tu-usuario/casa-cambio-mxn-usd)
![GitHub last commit](https://img.shields.io/github/last-commit/tu-usuario/casa-cambio-mxn-usd)

## ⭐ Si te gusta el proyecto

Si este proyecto te resulta útil, ¡dale una estrella! ⭐

También puedes:
- 🔄 Compartirlo con otros desarrolladores
- 🐛 Reportar bugs o sugerir mejoras
---

<div align="center">

**¿Encontraste útil este proyecto?**

[![GitHub stars](https://img.shields.io/github/stars/tu-usuario/casa-cambio-mxn-usd?style=social)](https://github.com/tu-usuario/casa-cambio-mxn-usd/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/tu-usuario/casa-cambio-mxn-usd?style=social)](https://github.com/tu-usuario/casa-cambio-mxn-usd/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/tu-usuario/casa-cambio-mxn-usd?style=social)](https://github.com/tu-usuario/casa-cambio-mxn-usd/watchers)

**Desarrollado con ❤️ en México 🇲🇽**

</div>
