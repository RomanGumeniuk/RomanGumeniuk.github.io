/* ================================================
   ATM10 TEAM GUIDE — MAIN JAVASCRIPT
   Interactions: cards, tabs, scroll, navigation
   ================================================ */

document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
    initHamburger();
    initRoleCards();
    initTipsTabs();
    initProgressionTabs();
    initScrollAnimations();
    initParticles();
    initTimelineProgress();
});

/* ---- NAVBAR ---- */
function initNavbar() {
    const navbar = document.getElementById('navbar');
    const navLinks = document.querySelectorAll('.nav-links a');
    const sections = document.querySelectorAll('.section');

    // Scroll background
    const handleScroll = () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Active section highlight
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - 120;
            const sectionBottom = sectionTop + section.offsetHeight;
            if (window.scrollY >= sectionTop && window.scrollY < sectionBottom) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('data-section') === current) {
                link.classList.add('active');
            }
        });
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();

    // Smooth scroll for nav links
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const target = document.getElementById(targetId);
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
                // Close mobile menu
                document.getElementById('navLinks').classList.remove('open');
                document.getElementById('hamburger').classList.remove('active');
                document.querySelector('.nav-overlay')?.classList.remove('active');
            }
        });
    });
}

/* ---- HAMBURGER MENU ---- */
function initHamburger() {
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');

    // Create overlay
    const overlay = document.createElement('div');
    overlay.classList.add('nav-overlay');
    document.body.appendChild(overlay);

    const toggleMenu = () => {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('open');
        overlay.classList.toggle('active');
    };

    hamburger.addEventListener('click', toggleMenu);
    overlay.addEventListener('click', toggleMenu);
}

/* ---- ROLE CARDS ---- */
function initRoleCards() {
    const cards = document.querySelectorAll('.role-card');

    cards.forEach(card => {
        const expandBtn = card.querySelector('.role-expand-btn');
        const closeBtn = card.querySelector('.role-close-btn');

        const toggleCard = (e) => {
            e.stopPropagation();
            const isActive = card.classList.contains('active');

            // Close all cards first
            cards.forEach(c => c.classList.remove('active'));

            // Toggle clicked card
            if (!isActive) {
                card.classList.add('active');

                // Update glow
                const color = card.getAttribute('data-color');
                card.style.setProperty('--active-color', color);

                // Scroll card into view with offset
                setTimeout(() => {
                    const cardTop = card.getBoundingClientRect().top + window.scrollY;
                    const offset = 80;
                    window.scrollTo({
                        top: cardTop - offset,
                        behavior: 'smooth'
                    });
                }, 100);
            }
        };

        expandBtn.addEventListener('click', toggleCard);
        card.querySelector('.role-card-header').addEventListener('click', toggleCard);

        if (closeBtn) {
            closeBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                card.classList.remove('active');
            });
        }
    });
}

/* ---- TIPS TABS ---- */
function initTipsTabs() {
    const tabs = document.querySelectorAll('.tip-tab');
    const panels = document.querySelectorAll('.tip-panel');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const target = tab.getAttribute('data-tip');

            // Update tabs
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            // Update panels
            panels.forEach(p => {
                p.classList.remove('active');
                if (p.getAttribute('data-tip-panel') === target) {
                    p.classList.add('active');
                }
            });
        });
    });
}

/* ---- PROGRESSION TABS (inside role cards) ---- */
function initProgressionTabs() {
    document.querySelectorAll('.progression-block').forEach(block => {
        const tabs = block.querySelectorAll('.prog-tab');
        const panels = block.querySelectorAll('.prog-panel');

        tabs.forEach(tab => {
            tab.addEventListener('click', (e) => {
                e.stopPropagation();
                const target = tab.getAttribute('data-tab');

                tabs.forEach(t => t.classList.remove('active'));
                tab.classList.add('active');

                panels.forEach(p => {
                    p.classList.remove('active');
                    if (p.getAttribute('data-panel') === target) {
                        p.classList.add('active');
                    }
                });
            });
        });
    });
}

/* ---- SCROLL ANIMATIONS ---- */
function initScrollAnimations() {
    // Add fade-in class to elements
    const animatableElements = [
        '.role-card',
        '.tips-tabs-wrapper',
        '.timeline-stage',
        '.section-header'
    ];

    animatableElements.forEach(selector => {
        document.querySelectorAll(selector).forEach(el => {
            el.classList.add('fade-in');
        });
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Stagger animation for grid items
                const parent = entry.target.parentElement;
                if (parent && parent.classList.contains('roles-grid')) {
                    const siblings = Array.from(parent.querySelectorAll('.role-card'));
                    const index = siblings.indexOf(entry.target);
                    entry.target.style.transitionDelay = `${index * 0.08}s`;
                }

                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -40px 0px'
    });

    document.querySelectorAll('.fade-in').forEach(el => {
        observer.observe(el);
    });
}

/* ---- HERO PARTICLES ---- */
function initParticles() {
    const container = document.getElementById('heroParticles');
    if (!container) return;

    const colors = ['#C8960C', '#AA44FF', '#4FC3F7', '#2D7A2D', '#FF4081'];
    const particleCount = 25;

    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.classList.add('hero-particle');
        particle.style.left = Math.random() * 100 + '%';
        particle.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        particle.style.animationDelay = Math.random() * 6 + 's';
        particle.style.animationDuration = (4 + Math.random() * 4) + 's';
        particle.style.width = (2 + Math.random() * 3) + 'px';
        particle.style.height = particle.style.width;
        container.appendChild(particle);
    }
}

/* ---- TIMELINE PROGRESS ---- */
function initTimelineProgress() {
    const timeline = document.querySelector('.timeline');
    const progress = document.getElementById('timelineProgress');
    if (!timeline || !progress) return;

    const updateProgress = () => {
        const timelineRect = timeline.getBoundingClientRect();
        const windowHeight = window.innerHeight;

        if (timelineRect.top < windowHeight && timelineRect.bottom > 0) {
            const visibleTop = Math.max(0, -timelineRect.top);
            const totalHeight = timelineRect.height;
            const percent = Math.min(100, (visibleTop / (totalHeight - windowHeight * 0.6)) * 100);
            progress.style.height = Math.max(0, percent) + '%';
        }
    };

    window.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();
}

/* ---- SMOOTH SCROLL FOR ALL ANCHOR LINKS ---- */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === '#') return;
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});
