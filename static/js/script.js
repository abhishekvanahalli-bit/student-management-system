document.addEventListener("DOMContentLoaded", () => {
    
    // --- 1. UI LOADER (PRIORITY) ---
    // Ensure loader disappears regardless of other script errors
    const hideLoader = () => {
        const loader = document.getElementById('page-loader');
        if (loader) {
            loader.classList.add('fade-out');
            setTimeout(() => { loader.style.display = 'none'; }, 500);
        }
    };
    // Trigger loader removal after a short delay
    setTimeout(hideLoader, 400);

    // --- 2. GLOBAL STATE & THEME ---
    const body = document.body;
    const themeSwitch = document.getElementById('checkbox');
    
    const settings = {
        theme: localStorage.getItem('theme') || 'auto',
        brightness: body.getAttribute('data-brightness') || localStorage.getItem('brightness') || 100,
        accent: body.getAttribute('data-accent') || localStorage.getItem('accent') || '#4e73df'
    };

    // Theme Application Function
    const applyTheme = (mode) => {
        if (mode === 'dark') {
            body.classList.add('dark-mode');
            if (themeSwitch) themeSwitch.checked = true;
        } else if (mode === 'light') {
            body.classList.remove('dark-mode');
            if (themeSwitch) themeSwitch.checked = false;
        } else {
            // Auto mode
            const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            body.classList.toggle('dark-mode', prefersDark);
            if (themeSwitch) themeSwitch.checked = prefersDark;
        }
        localStorage.setItem('theme', mode);
    };

    // Brightness Application
    const applyBrightness = (val) => {
        const overlay = document.getElementById('brightness-overlay');
        if (overlay) {
            const opacity = (100 - val) / 100;
            overlay.style.backgroundColor = `rgba(0, 0, 0, ${opacity})`;
        }
        localStorage.setItem('brightness', val);
    };

    // Initial Setup
    applyTheme(settings.theme);
    applyBrightness(settings.brightness);

    // --- 3. EVENT LISTENERS ---

    // Dark Mode Toggle (Navbar)
    if (themeSwitch) {
        themeSwitch.addEventListener('change', (e) => {
            applyTheme(e.target.checked ? 'dark' : 'light');
        });
    }

    // Settings Page Specific Listeners
    const themeSelect = document.querySelector('select[name="theme_mode"]');
    if (themeSelect) {
        themeSelect.value = settings.theme;
        themeSelect.addEventListener('change', (e) => applyTheme(e.target.value));
    }

    const brightnessInput = document.querySelector('input[name="brightness"]');
    if (brightnessInput) {
        brightnessInput.addEventListener('input', (e) => applyBrightness(e.target.value));
    }

    // Sidebar Toggle
    const sidebarCollapse = document.getElementById('sidebarCollapse');
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebar-overlay'); // New overlay element

    if (sidebarCollapse && sidebar) {
        sidebarCollapse.addEventListener('click', () => {
            // Check if it's a mobile view
            if (window.innerWidth <= 768) {
                sidebar.classList.toggle('show'); // Toggle mobile slide-in/out
                if (overlay) overlay.classList.toggle('show');
            } else {
                sidebar.classList.toggle('sidebar-collapsed'); // Toggle desktop collapse/expand
                body.classList.toggle('sidebar-collapsed'); // Adjust main content for desktop
            }
        });
    }

    // Close mobile sidebar when clicking outside
    if (overlay) {
        overlay.addEventListener('click', () => {
            sidebar.classList.remove('show');
            overlay.classList.remove('show');
        });
    }

    // Close mobile sidebar when clicking a link
    const sidebarLinks = document.querySelectorAll('#sidebar .sidebar-link');
    sidebarLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth <= 768) {
                sidebar.classList.remove('show');
                if (overlay) overlay.classList.remove('show');
            }
        });
    });

    // File Upload Previews
    const fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(input => {
        input.addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (event) => {
                    const preview = input.closest('.mb-3')?.querySelector('img') || 
                                    input.closest('.card')?.querySelector('img');
                    if (preview) preview.src = event.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
    });

    // Animated Counters (Dashboard)
    const counters = document.querySelectorAll('.counter-value');
    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        const updateCount = () => {
            const count = +counter.innerText;
            const inc = target / 100;
            if (count < target) {
                counter.innerText = Math.ceil(count + inc);
                setTimeout(updateCount, 20);
            } else {
                counter.innerText = target;
            }
        };
        if (target > 0) updateCount();
    });
});
