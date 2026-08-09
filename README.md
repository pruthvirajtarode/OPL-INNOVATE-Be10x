# Microsoft Copilot Training Module

**OPL INNOVATE × Be10x**
**Day 2: AI Across the Microsoft Workflow (3 Hours)**

This is a complete, offline-first interactive training application designed for working professionals in IT & Product teams.

## Project Overview
This application delivers a premium, hands-on learning experience focused on integrating Microsoft Copilot into daily workflows. It is built as a static web application and requires no internet connection, backend server, or database to run, making it ideal for corporate training environments.

## Session Structure (3 Hours)
- **Module 1**: Meet Copilot (0:10 - 0:30)
- **Module 2**: Copilot Inside Daily Apps (Outlook, Word, Excel, PowerPoint, Teams) (0:30 - 1:30)
- **Module 3**: Cross-App & Advanced Workflows (1:40 - 2:30)
- **Capstone**: Real Work Problem (2:30 - 2:50)
- **Showcase & Q&A**: (2:50 - 3:00)

## How to Run
1. Open `index.html` in any modern web browser (Chrome, Edge, Firefox).
2. Use the **START SESSION** button to launch the interactive deck.
3. No build step or local server is required.

## Key Features
### 1. Trainer Mode
A hidden dashboard for the facilitator.
- **How to activate**: Press `Shift + T` at any time while viewing the deck, or click "TRAINER MODE" from the landing page.
- **What it does**: Overlays facilitator notes, pacing suggestions, expected answers, common mistakes, and "rescue lines" on top of the current slide.

### 2. Participant Mode & Workbook
Participants can follow along using the digital workbook located at `workbook/index.html`.
- **Persistence**: All inputs are saved locally to the browser's `localStorage`. If the participant refreshes the page, their work remains.
- **Printable**: The workbook is designed to be easily printed (Ctrl+P / Cmd+P) for offline use.

### 3. Synthetic Data Pack
All examples use realistic but completely synthetic (fake) corporate data located in the `data/` folder. This ensures no confidential information is exposed during training.

### 4. Keyboard Navigation (Deck)
- `Right Arrow` / `Space`: Next slide
- `Left Arrow`: Previous slide
- `Home`: First slide
- `End`: Last slide
- `F`: Toggle Fullscreen
- `Shift + T`: Toggle Trainer Mode
- `Esc`: Exit Fullscreen

## Microsoft Capability Disclaimer
> Copilot features, integrations and availability may vary by Microsoft 365 license, tenant configuration, permissions and product version.

The training does not fabricate Microsoft product capabilities. Capabilities that rely on specific licensing or tenant configuration are explicitly called out during the session.

## How to Reset
To clear all saved progress (timer states, workbook entries, etc.):
1. Open Developer Tools in your browser (F12).
2. Go to the Application / Storage tab.
3. Clear `Local Storage`.
4. Refresh the page.
(Alternatively, use the "Reset Session" button available in the workbook footer).

## QA Checklist
- [x] Offline mode works (no external dependencies)
- [x] Responsive layout (tested on 1920x1080, 1440x900)
- [x] Keyboard navigation
- [x] Trainer mode toggles
- [x] Workbook data persistence
