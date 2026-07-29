/* City General Hospital – Main JavaScript */

// === Mobile Nav Toggle ===
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');

if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.toggle('open');
        const isOpen = navMenu.classList.contains('open');
        navToggle.setAttribute('aria-expanded', isOpen);
    });

    // Close menu on link click
    navMenu.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => navMenu.classList.remove('open'));
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
        if (!navToggle.contains(e.target) && !navMenu.contains(e.target)) {
            navMenu.classList.remove('open');
        }
    });
}

// === Auto-dismiss flash messages ===
setTimeout(() => {
    document.querySelectorAll('.flash').forEach(f => {
        f.style.transition = 'opacity 0.5s';
        f.style.opacity = '0';
        setTimeout(() => f.remove(), 500);
    });
}, 5000);

// === Skill bar animation (portfolio page) ===
const skillFills = document.querySelectorAll('.skill-fill');
if (skillFills.length > 0) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.width = entry.target.dataset.width || entry.target.style.width;
            }
        });
    }, { threshold: 0.1 });
    skillFills.forEach(el => observer.observe(el));
}

// === Form validation ===
document.querySelectorAll('form[novalidate]').forEach(form => {
    form.addEventListener('submit', function (e) {
        let valid = true;
        form.querySelectorAll('[required]').forEach(input => {
            if (!input.value.trim()) {
                valid = false;
                input.style.borderColor = '#dc2626';
                input.addEventListener('input', () => input.style.borderColor = '', { once: true });
            }
        });
        if (!valid) {
            e.preventDefault();
            const first = form.querySelector('[required]:invalid, [required][style*="dc2626"]');
            if (first) first.focus();
        }
    });
});

// === Smooth scroll for anchor links ===
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});
