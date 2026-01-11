# Prompt for Claude Opus (Specification)

**Role:** Creative Frontend Developer & UX Engineer
**Project:** "Quarter" Luxury Landing Page - Magnolia Variant
**Objective:** Refine the current HTML/JS prototype into a production-ready, Awwwards-level mobile experience.

---

## Context & Current State
We have a single-file HTML prototype.
- **Visuals:** Uses a rotated high-res background photo, distinct typography, and a "Cinematic Drift" animation.
- **Atmosphere:** Canvas-based dust particles.
- **Interaction:** A hidden object game where the user collects 3 "Magic Orbs" to reveal a discount code.
- **Target Audience:** Premium/Luxury consumers (Mobile-first).

## Technical Specification for Improvements

Please update the code to implement the following features:

### 1. Advanced Atmosphere (The "Film Look")
- **Noise Overlay:** Implement a lightweight SVG or Canvas-based noise filter (`opacity: 0.05-0.1`) overlaying the entire screen. This adds texture and simulates film grain, essential for the "Old Money" aesthetic.
- **Dynamic Lighting:** Create a "vignette" or "spotlight" layer that subtly follows the user's cursor (on desktop) or moves automatically (on mobile) to illuminate parts of the dark background.

### 2. Organic "Firefly" Physics
- **Refactor Orbs:** Move the "Magic Orbs" logic from CSS Keyframes to a JavaScript-based physics model (e.g., using Perlin Noise or sinusoidal vectors) so their movement looks unpredictable and organic (like real insects/will-o'-the-wisps).
- **Magnetic Interaction:** Implement a "soft magnet" effect where orbs gently drift towards the user's touch/cursor when nearby, making the collection process feel more satisfying.
- **Trail Effect:** (Optional) Add a faint, fading trail behind the orbs using Canvas.

### 3. Mobile Immersion (Gyroscope Parallax)
- **Depth:** Implement a parallax effect using `DeviceOrientationEvent` (with a fallback to mouse movement).
    - **Layer 1 (Bg):** Moves slightly in opposition to tilt.
    - **Layer 2 (Dust):** Moves faster than Bg.
    - **Layer 3 (UI):** Static.
- This creates a "Window into the garden" effect on mobile devices.

### 4. Micro-Interactions & Audio
- **Haptic Patterns:** Refine the `navigator.vibrate` patterns (e.g., a "double heartbeat" pulse when an orb is caught).
- **Sound Hooks:** Prepare placeholders or functional Web Audio API calls for:
    - *Loop:* Subtle night ambience (crickets/wind).
    - *SFX:* Soft chime when an orb is collected.

### 5. Code Quality
- Refactor the script into clean Classes (`App`, `ParticleSystem`, `OrbManager`).
- Ensure `requestAnimationFrame` is used for all visual updates to maintain 60fps.

---

**Instruction:** 
Take the existing code (provided below), apply these improvements, and output the single refined HTML file. Focus heavily on code cleanliness and smooth animations.
