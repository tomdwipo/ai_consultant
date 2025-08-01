// AI Media Consultant Landing Page JavaScript
// Modern ES6+ JavaScript with performance optimization

class LandingPage {
    constructor() {
        this.init();
        this.bindEvents();
        this.setupIntersectionObserver();
        this.setupStickyNavbar();
        this.setupStickyCtA();
        this.setupFormHandling();
        this.setupAnimations();
    }

    init() {
        // Initialize variables
        this.navbar = document.getElementById('navbar');
        this.navToggle = document.getElementById('nav-toggle');
        this.navMenu = document.getElementById('nav-menu');
        this.stickyCtA = document.getElementById('sticky-cta');
        this.leadMagnetForm = document.getElementById('leadMagnetForm');
        this.successModal = document.getElementById('successModal');

        // Performance optimization: Use passive listeners where possible
        this.passiveSupported = this.checkPassiveSupport();

        // Throttle scroll events for better performance
        this.scrollThrottled = this.throttle(this.handleScroll.bind(this), 16);

        // Initialize page state
        this.isMenuOpen = false;
        this.lastScrollY = window.scrollY;

        console.log('🤖 AI Media Consultant Landing Page Initialized');
    }

    bindEvents() {
        // Navigation events
        this.navToggle?.addEventListener('click', this.toggleMobileMenu.bind(this));

        // Close mobile menu when clicking nav links
        const navLinks = document.querySelectorAll('.nav-link, .nav-cta');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (this.isMenuOpen) {
                    this.toggleMobileMenu();
                }
            });
        });

        // Scroll events with throttling
        window.addEventListener('scroll', this.scrollThrottled,
            this.passiveSupported ? { passive: true } : false);

        // Resize events with debouncing
        window.addEventListener('resize', this.debounce(this.handleResize.bind(this), 250));

        // Form submission
        this.leadMagnetForm?.addEventListener('submit', this.handleFormSubmit.bind(this));

        // Modal events
        const modalClose = document.querySelector('.modal-close');
        modalClose?.addEventListener('click', this.closeModal.bind(this));

        // Close modal when clicking outside
        this.successModal?.addEventListener('click', (e) => {
            if (e.target === this.successModal) {
                this.closeModal();
            }
        });

        // Keyboard navigation
        document.addEventListener('keydown', this.handleKeydown.bind(this));

        // Smooth scroll for anchor links
        document.addEventListener('click', this.handleSmoothScroll.bind(this));
    }

    setupIntersectionObserver() {
        // Animate elements when they come into view
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        this.observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');

                    // Special handling for stats counter animation
                    if (entry.target.classList.contains('stat-number')) {
                        this.animateCounter(entry.target);
                    }
                }
            });
        }, observerOptions);

        // Observe elements for animation
        const animateElements = document.querySelectorAll(
            '.feature-card, .testimonial-card, .problem-card, .stat-card, .pricing-card'
        );

        animateElements.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
            this.observer.observe(el);
        });
    }

    setupStickyNavbar() {
        // Add/remove navbar background on scroll
        const handleNavbarScroll = () => {
            if (window.scrollY > 50) {
                this.navbar?.classList.add('scrolled');
            } else {
                this.navbar?.classList.remove('scrolled');
            }
        };

        window.addEventListener('scroll', this.throttle(handleNavbarScroll, 16),
            this.passiveSupported ? { passive: true } : false);
    }

    setupStickyCtA() {
        // Show/hide sticky CTA based on scroll position
        const heroSection = document.getElementById('hero');
        const leadMagnetSection = document.getElementById('lead-magnet');

        if (!heroSection || !leadMagnetSection || !this.stickyCtA) return;

        const handleStickyCtA = () => {
            const heroBottom = heroSection.offsetTop + heroSection.offsetHeight;
            const leadMagnetTop = leadMagnetSection.offsetTop;
            const scrollY = window.scrollY;

            if (scrollY > heroBottom && scrollY < leadMagnetTop - 200) {
                this.stickyCtA.classList.add('visible');
            } else {
                this.stickyCtA.classList.remove('visible');
            }
        };

        window.addEventListener('scroll', this.throttle(handleStickyCtA, 16),
            this.passiveSupported ? { passive: true } : false);
    }

    setupFormHandling() {
        // Enhanced form validation and UX
        const formInputs = this.leadMagnetForm?.querySelectorAll('input, select');

        formInputs?.forEach(input => {
            // Real-time validation feedback
            input.addEventListener('blur', () => this.validateField(input));
            input.addEventListener('input', () => this.clearFieldError(input));
        });
    }

    setupAnimations() {
        // Add CSS classes for animations when elements are in view
        const style = document.createElement('style');
        style.textContent = `
            .animate-in {
                opacity: 1 !important;
                transform: translateY(0) !important;
            }
            
            .navbar.scrolled {
                background: rgba(255, 255, 255, 0.98) !important;
                backdrop-filter: blur(20px);
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            }
            
            .field-error {
                border-color: #dc2626 !important;
                box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1) !important;
            }
            
            .field-success {
                border-color: #059669 !important;
                box-shadow: 0 0 0 3px rgba(5, 150, 105, 0.1) !important;
            }
        `;
        document.head.appendChild(style);
    }

    // Event Handlers
    toggleMobileMenu() {
        this.isMenuOpen = !this.isMenuOpen;
        this.navMenu?.classList.toggle('active');
        this.navToggle?.classList.toggle('active');

        // Prevent body scroll when menu is open
        document.body.style.overflow = this.isMenuOpen ? 'hidden' : '';

        // Accessibility
        this.navToggle?.setAttribute('aria-expanded', this.isMenuOpen.toString());
    }

    handleScroll() {
        const currentScrollY = window.scrollY;

        // Hide/show navbar on scroll direction
        if (currentScrollY > this.lastScrollY && currentScrollY > 100) {
            this.navbar?.classList.add('nav-hidden');
        } else {
            this.navbar?.classList.remove('nav-hidden');
        }

        this.lastScrollY = currentScrollY;
    }

    handleResize() {
        // Close mobile menu on resize to desktop
        if (window.innerWidth > 768 && this.isMenuOpen) {
            this.toggleMobileMenu();
        }
    }

    handleFormSubmit(e) {
        e.preventDefault();

        if (!this.validateForm()) {
            return;
        }

        // Show loading state
        const submitButton = this.leadMagnetForm.querySelector('button[type="submit"]');
        const originalText = submitButton.textContent;

        submitButton.textContent = 'Mengirim...';
        submitButton.disabled = true;
        submitButton.classList.add('loading');

        // Simulate form submission (replace with actual API call)
        this.submitForm()
            .then(() => {
                this.showSuccessModal();
                this.leadMagnetForm.reset();
                this.trackConversion('lead_magnet_download');
            })
            .catch((error) => {
                console.error('Form submission error:', error);
                this.showErrorMessage('Terjadi kesalahan. Silakan coba lagi.');
            })
            .finally(() => {
                submitButton.textContent = originalText;
                submitButton.disabled = false;
                submitButton.classList.remove('loading');
            });
    }

    handleKeydown(e) {
        // Escape key closes modal and mobile menu
        if (e.key === 'Escape') {
            if (this.successModal?.classList.contains('active')) {
                this.closeModal();
            }
            if (this.isMenuOpen) {
                this.toggleMobileMenu();
            }
        }
    }

    handleSmoothScroll(e) {
        // Handle smooth scrolling for anchor links
        const target = e.target.closest('a[href^="#"]');
        if (!target) return;

        const href = target.getAttribute('href');
        if (href === '#') return;

        e.preventDefault();
        this.scrollToSection(href.substring(1));
    }

    // Form Validation
    validateForm() {
        const formData = new FormData(this.leadMagnetForm);
        let isValid = true;

        // Validate required fields
        const requiredFields = ['fullName', 'email', 'businessType', 'businessSize'];

        requiredFields.forEach(fieldName => {
            const field = this.leadMagnetForm.querySelector(`[name="${fieldName}"]`);
            const value = formData.get(fieldName);

            if (!value || value.trim() === '') {
                this.showFieldError(field, 'Field ini wajib diisi');
                isValid = false;
            } else if (fieldName === 'email' && !this.isValidEmail(value)) {
                this.showFieldError(field, 'Format email tidak valid');
                isValid = false;
            } else {
                this.showFieldSuccess(field);
            }
        });

        return isValid;
    }

    validateField(field) {
        const value = field.value.trim();
        const fieldName = field.name;

        if (!value) {
            this.showFieldError(field, 'Field ini wajib diisi');
            return false;
        }

        if (fieldName === 'email' && !this.isValidEmail(value)) {
            this.showFieldError(field, 'Format email tidak valid');
            return false;
        }

        if (fieldName === 'fullName' && value.length < 2) {
            this.showFieldError(field, 'Nama minimal 2 karakter');
            return false;
        }

        this.showFieldSuccess(field);
        return true;
    }

    showFieldError(field, message) {
        field.classList.add('field-error');
        field.classList.remove('field-success');

        // Remove existing error message
        const existingError = field.parentNode.querySelector('.field-error-message');
        if (existingError) {
            existingError.remove();
        }

        // Add error message
        const errorDiv = document.createElement('div');
        errorDiv.className = 'field-error-message';
        errorDiv.style.cssText = 'color: #dc2626; font-size: 0.875rem; margin-top: 0.25rem;';
        errorDiv.textContent = message;
        field.parentNode.appendChild(errorDiv);
    }

    showFieldSuccess(field) {
        field.classList.remove('field-error');
        field.classList.add('field-success');

        // Remove error message
        const errorMessage = field.parentNode.querySelector('.field-error-message');
        if (errorMessage) {
            errorMessage.remove();
        }
    }

    clearFieldError(field) {
        field.classList.remove('field-error');
        const errorMessage = field.parentNode.querySelector('.field-error-message');
        if (errorMessage) {
            errorMessage.remove();
        }
    }

    showErrorMessage(message) {
        // Create and show error notification
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-notification';
        errorDiv.style.cssText = `
            position: fixed;
            top: 100px;
            right: 20px;
            background: #dc2626;
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 0.5rem;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            z-index: 1001;
            animation: slideInRight 0.3s ease-out;
        `;
        errorDiv.textContent = message;

        document.body.appendChild(errorDiv);

        setTimeout(() => {
            errorDiv.remove();
        }, 5000);
    }

    // Modal Management
    showSuccessModal() {
        this.successModal?.classList.add('active');
        document.body.style.overflow = 'hidden';

        // Focus management for accessibility
        const firstFocusable = this.successModal?.querySelector('button');
        firstFocusable?.focus();
    }

    closeModal() {
        this.successModal?.classList.remove('active');
        document.body.style.overflow = '';
    }

    // Utility Functions
    scrollToSection(sectionId) {
        const section = document.getElementById(sectionId);
        if (!section) return;

        const navbarHeight = this.navbar?.offsetHeight || 80;
        const targetPosition = section.offsetTop - navbarHeight;

        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });

        // Update URL without triggering navigation
        if (history.pushState) {
            history.pushState(null, null, `#${sectionId}`);
        }
    }

    animateCounter(element) {
        const target = parseInt(element.textContent.replace(/[^\d]/g, ''));
        const duration = 2000;
        const step = target / (duration / 16);
        let current = 0;

        const updateCounter = () => {
            current += step;
            if (current < target) {
                element.textContent = this.formatNumber(Math.floor(current));
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = this.formatNumber(target);
            }
        };

        updateCounter();
    }

    formatNumber(num) {
        if (num >= 1000) {
            return (num / 1000).toFixed(1) + 'K+';
        }
        return num.toString();
    }

    async submitForm() {
        // Simulate API call - replace with actual endpoint
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                // Simulate success (90% success rate for demo)
                if (Math.random() > 0.1) {
                    resolve({ success: true });
                } else {
                    reject(new Error('Network error'));
                }
            }, 1500);
        });
    }

    trackConversion(eventName) {
        // Analytics tracking - replace with actual implementation
        if (typeof gtag !== 'undefined') {
            gtag('event', 'conversion', {
                'send_to': 'AW-CONVERSION_ID/CONVERSION_LABEL',
                'event_category': 'Lead Generation',
                'event_label': eventName
            });
        }

        // Facebook Pixel tracking
        if (typeof fbq !== 'undefined') {
            fbq('track', 'Lead', {
                content_name: 'Lead Magnet Download',
                content_category: 'Content Marketing Guide'
            });
        }

        console.log(`🎯 Conversion tracked: ${eventName}`);
    }

    isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    throttle(func, limit) {
        let inThrottle;
        return function () {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }

    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    checkPassiveSupport() {
        let passiveSupported = false;
        try {
            const options = {
                get passive() {
                    passiveSupported = true;
                    return false;
                }
            };
            window.addEventListener('test', null, options);
            window.removeEventListener('test', null, options);
        } catch (err) {
            passiveSupported = false;
        }
        return passiveSupported;
    }
}

// Global Functions (for inline event handlers)
function scrollToSection(sectionId) {
    if (window.landingPageApp) {
        window.landingPageApp.scrollToSection(sectionId);
    }
}

function closeModal() {
    if (window.landingPageApp) {
        window.landingPageApp.closeModal();
    }
}

// Performance Optimization: Load non-critical features after page load
function loadNonCriticalFeatures() {
    // Lazy load images
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));

    // Load analytics scripts
    loadAnalytics();
}

function loadAnalytics() {
    // Google Analytics 4
    if (!window.gtag) {
        const script = document.createElement('script');
        script.async = true;
        script.src = 'https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID';
        document.head.appendChild(script);

        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());
        gtag('config', 'GA_MEASUREMENT_ID');
        window.gtag = gtag;
    }

    // Facebook Pixel (if needed)
    // Add Facebook Pixel code here
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        window.landingPageApp = new LandingPage();

        // Load non-critical features after a delay
        setTimeout(loadNonCriticalFeatures, 1000);
    });
} else {
    window.landingPageApp = new LandingPage();
    setTimeout(loadNonCriticalFeatures, 1000);
}

// Service Worker Registration for PWA capabilities (optional)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}

// Export for module systems (if needed)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = LandingPage;
}