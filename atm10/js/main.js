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
    initSearch();
    initFAQ();
    initCopyButtons();
    initBackToTop();
    initOptBarAnimations();
    initModCategoryTabs();
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
        '.section-header',
        '.dimension-card',
        '.cheat-card',
        '.faq-item'
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

/* ---- SEARCH ---- */
function initSearch() {
    const searchToggle = document.getElementById('searchToggle');
    const searchOverlay = document.getElementById('searchOverlay');
    const searchInput = document.getElementById('searchInput');
    const searchClose = document.getElementById('searchClose');
    const searchResults = document.getElementById('searchResults');

    if (!searchToggle || !searchOverlay) return;

    // Build search index from page content
    const searchIndex = [];

    // Index role cards
    document.querySelectorAll('.role-card').forEach(card => {
        const name = card.querySelector('.role-name')?.textContent || '';
        const tagline = card.querySelector('.role-tagline')?.textContent || '';
        const details = card.querySelector('.role-details-inner')?.textContent || '';
        searchIndex.push({
            section: 'Rola: ' + name,
            text: name + ' ' + tagline + ' ' + details,
            target: '#roles'
        });
    });

    // Index tips
    document.querySelectorAll('.tip-panel').forEach(panel => {
        const title = panel.querySelector('h3')?.textContent || '';
        const content = panel.textContent || '';
        searchIndex.push({
            section: 'Pro Tipy: ' + title,
            text: content,
            target: '#tips'
        });
    });

    // Index dimensions
    document.querySelectorAll('.dimension-card').forEach(card => {
        const name = card.querySelector('h3')?.textContent || '';
        const content = card.textContent || '';
        searchIndex.push({
            section: 'Wymiar: ' + name,
            text: content,
            target: '#dimensions'
        });
    });

    // Index cheat sheet
    document.querySelectorAll('.cheat-card').forEach(card => {
        const name = card.querySelector('h3')?.textContent || '';
        const content = card.textContent || '';
        searchIndex.push({
            section: 'Cheat Sheet: ' + name,
            text: content,
            target: '#cheatsheet'
        });
    });

    // Index FAQ
    document.querySelectorAll('.faq-item').forEach(item => {
        const question = item.querySelector('.faq-question span')?.textContent || '';
        const answer = item.querySelector('.faq-answer')?.textContent || '';
        searchIndex.push({
            section: 'FAQ',
            text: question + ' ' + answer,
            target: '#faq'
        });
    });

    // Index progression
    document.querySelectorAll('.timeline-stage').forEach(stage => {
        const label = stage.querySelector('.stage-label')?.textContent || '';
        const content = stage.textContent || '';
        searchIndex.push({
            section: 'Progresja: ' + label,
            text: content,
            target: '#progression'
        });
    });

    // Index mod encyclopedia
    document.querySelectorAll('.mod-encyclopedia-card').forEach(card => {
        const name = card.querySelector('h3')?.textContent || '';
        const content = card.textContent || '';
        searchIndex.push({
            section: 'Mod: ' + name,
            text: content,
            target: '#modguide'
        });
    });

    // Index boss guide
    document.querySelectorAll('.boss-card').forEach(card => {
        const name = card.querySelector('h3')?.textContent || '';
        const content = card.textContent || '';
        searchIndex.push({
            section: 'Boss: ' + name,
            text: content,
            target: '#bosses'
        });
    });

    const openSearch = () => {
        searchOverlay.classList.add('active');
        setTimeout(() => searchInput.focus(), 200);
        document.body.style.overflow = 'hidden';
    };

    const closeSearch = () => {
        searchOverlay.classList.remove('active');
        searchInput.value = '';
        searchResults.innerHTML = '<p class="search-hint">Wpisz minimum 2 znaki aby wyszukać...</p>';
        document.body.style.overflow = '';
    };

    searchToggle.addEventListener('click', openSearch);
    searchClose.addEventListener('click', closeSearch);
    searchOverlay.addEventListener('click', (e) => {
        if (e.target === searchOverlay) closeSearch();
    });

    // Keyboard shortcut: Ctrl+K
    document.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            openSearch();
        }
        if (e.key === 'Escape') {
            closeSearch();
        }
    });

    searchInput.addEventListener('input', () => {
        const query = searchInput.value.trim().toLowerCase();
        if (query.length < 2) {
            searchResults.innerHTML = '<p class="search-hint">Wpisz minimum 2 znaki aby wyszukać...</p>';
            return;
        }

        const results = searchIndex.filter(item => 
            item.text.toLowerCase().includes(query)
        );

        if (results.length === 0) {
            searchResults.innerHTML = '<p class="search-hint">Brak wyników dla "' + query + '"</p>';
            return;
        }

        searchResults.innerHTML = results.slice(0, 8).map(result => {
            // Find context around match
            const idx = result.text.toLowerCase().indexOf(query);
            const start = Math.max(0, idx - 40);
            const end = Math.min(result.text.length, idx + query.length + 60);
            let snippet = result.text.substring(start, end).trim();
            if (start > 0) snippet = '...' + snippet;
            if (end < result.text.length) snippet += '...';

            // Highlight match
            const escapedQuery = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
            const highlighted = snippet.replace(new RegExp(escapedQuery, 'gi'), '<mark>$&</mark>');

            return `<div class="search-result-item" data-target="${result.target}">
                <div class="result-section">${result.section}</div>
                <div class="result-text">${highlighted}</div>
            </div>`;
        }).join('');

        // Add click handlers
        searchResults.querySelectorAll('.search-result-item').forEach(item => {
            item.addEventListener('click', () => {
                const target = document.querySelector(item.dataset.target);
                if (target) {
                    closeSearch();
                    setTimeout(() => target.scrollIntoView({ behavior: 'smooth' }), 100);
                }
            });
        });
    });
}

/* ---- FAQ ACCORDION ---- */
function initFAQ() {
    document.querySelectorAll('.faq-item').forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');

        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');

            // Close all
            document.querySelectorAll('.faq-item').forEach(i => {
                i.classList.remove('active');
                i.querySelector('.faq-answer').style.maxHeight = '0';
            });

            // Toggle clicked
            if (!isActive) {
                item.classList.add('active');
                answer.style.maxHeight = answer.scrollHeight + 'px';
            }
        });
    });
}

/* ---- COPY BUTTONS ---- */
function initCopyButtons() {
    document.querySelectorAll('.copy-btn').forEach(btn => {
        btn.addEventListener('click', async () => {
            const commandItem = btn.closest('.command-item');
            const code = commandItem.querySelector('.cmd-code');
            const text = code.getAttribute('data-copy') || code.textContent;

            try {
                await navigator.clipboard.writeText(text);
                btn.classList.add('copied');
                btn.innerHTML = '<i class="fas fa-check"></i>';
                
                setTimeout(() => {
                    btn.classList.remove('copied');
                    btn.innerHTML = '<i class="fas fa-copy"></i>';
                }, 2000);
            } catch (err) {
                // Fallback
                const textarea = document.createElement('textarea');
                textarea.value = text;
                document.body.appendChild(textarea);
                textarea.select();
                document.execCommand('copy');
                document.body.removeChild(textarea);

                btn.classList.add('copied');
                btn.innerHTML = '<i class="fas fa-check"></i>';
                setTimeout(() => {
                    btn.classList.remove('copied');
                    btn.innerHTML = '<i class="fas fa-copy"></i>';
                }, 2000);
            }
        });
    });
}

/* ---- BACK TO TOP ---- */
function initBackToTop() {
    const btn = document.getElementById('backToTop');
    if (!btn) return;

    const toggleBtn = () => {
        if (window.scrollY > 500) {
            btn.classList.add('visible');
        } else {
            btn.classList.remove('visible');
        }
    };

    window.addEventListener('scroll', toggleBtn, { passive: true });

    btn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

/* ---- OPTIMIZATION BAR ANIMATIONS ---- */
function initOptBarAnimations() {
    const optBars = document.querySelectorAll('.opt-fill');
    if (!optBars.length) return;

    // Store original widths and reset
    optBars.forEach(bar => {
        bar.dataset.targetWidth = bar.style.width;
        bar.style.width = '0%';
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const bar = entry.target;
                setTimeout(() => {
                    bar.style.width = bar.dataset.targetWidth;
                }, 200);
                observer.unobserve(bar);
            }
        });
    }, { threshold: 0.5 });

    optBars.forEach(bar => observer.observe(bar));
}

/* ---- MOD CATEGORY TABS ---- */
function initModCategoryTabs() {
    const tabs = document.querySelectorAll('.mod-cat-tab');
    const panels = document.querySelectorAll('.mod-cat-panel');

    if (!tabs.length || !panels.length) return;

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const cat = tab.getAttribute('data-modcat');

            // Update tabs
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            // Update panels
            panels.forEach(p => {
                p.classList.remove('active');
                if (p.getAttribute('data-modcat-panel') === cat) {
                    p.classList.add('active');
                }
            });
        });
    });
}
