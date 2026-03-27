# /onboard — Workspace Initialization

Welcome! I'm your Expo debugging partner. Let me learn about your app and environment so I can give you the most targeted help possible.

## Interview Flow

Ask the following questions one section at a time. Wait for answers before proceeding.

### Section 1: Your App

1. What's your app called, and what does it do in one sentence?
2. Which Expo SDK version are you using? (check with `npx expo --version` or look in package.json)
3. Are you using Expo Router or React Navigation for navigation?
4. Is there anything unusual about your project structure? (monorepo, shared packages, etc.)

### Section 2: Your Backend

1. What framework is your Railway backend built with? (Express, Fastify, NestJS, etc.)
2. What database are you using? (PostgreSQL on Railway, Supabase, Firebase, etc.)
3. How does your app authenticate users? (Firebase Auth, Clerk, custom JWT, etc.)
4. Is your API REST, GraphQL, or something else?

### Section 3: Your Environment

1. What computer are you developing on? (Mac model, macOS version)
2. What's your Node.js version? (`node -v`)
3. Are you using npm, yarn, or pnpm?
4. Do you test primarily in Expo Go, a development build, or the iOS Simulator?
5. Have you set up EAS Build for production builds?

### Section 4: Current Pain Points

1. What are the top 2-3 bugs or issues currently frustrating you?
2. Are there any errors you see repeatedly?
3. Is there a particular area of the app where things tend to break?

## After Gathering Answers

1. Update `context/project.md` with app details
2. Update `context/role.md` with any additional preferences
3. Update `context/for-agent/environment.md` with environment specifics
4. Log the onboarding session to `work-log/` with today's date
5. Summarize what you learned and suggest starting with `/triage` on the most critical current bug
