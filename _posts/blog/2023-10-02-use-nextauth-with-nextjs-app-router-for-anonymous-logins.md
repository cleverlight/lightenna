---
layout: single
title: Use NextAuth (Auth.js) for both anonymous and GitHub-authenticated logins
description: Next.js new App router opens up new opportunities for server-side optimised app delivery
tags: tech front apps
toc: true
header:
    overlay_image: /assets/images/app_router_nextjs_18980_04494_1920x.jpg
    small_image: /assets/images/app_router_nextjs_18980_04494_640x.jpg
---

## Repo
All the code in this article is available [open-source in our GitHub repo](https://github.com/lightenna/nextjs-app-auth-anon-logins-example).

## Introduction
This is an example of using next.js, nextauth.js and typescript for both anonymous sessions and authenticated sessions.  It's not a primer on how to use Next.js or Nextauth.js, but the focus instead is how to resolve a specific problem.

The basis of this demo is a simple OAuth login using Github as a provider.  It's from an app that allows users to [update notes stored in GitHub](https://www.notegit.com/).  Users can't do that without a GitHub user.  However, I wanted to enable users to test the app before logging in.  To do that we need to manage information before having an authenticate user account.

To achieve that anonymous user experience we need a session, as the user hasn't logged in yet.  This demo creates an anonymous session using a second `provider`.  It's not polished.  It simply shows the session information, specifically how:

* It starts with an empty state (no data)
* It's replaced by an anonymous session automatically, typically within a few seconds
* When the user clicks `Sign in`, they're redirected to GitHub
* After they're redirected back, selected GitHub user details are visible in the session
* When the user clicks `Sign out`, the session is wiped (no data).
* Again, within a few seconds, a new anonymous session is created and displayed.

## Getting started

* First install the repo
  ```
  npm install
  npm run gen-secret
  ```
* Set up `.env.local` using placeholders from `.env.local.template`
  * Include the `NEXTAUTH_SECRET` generated above
  * Transpose credentials from your (already created) GitHub App
* Run locally
  ```
  npm run dev
  ```
* Open a browser to http://localhost:3000
* Click `Sign in` button
  * View logs to see `GitHub signIn` event
* Click `Sign out` button
  * View logs to see `GitHub signOut` and `Anonymous signIn` events

## Highlights
The `/editor` route is wrapped in a NextAuthProvider:

```
<NextAuthProvider>
    <section>
        <nav>
            <Account/>
        </nav>
        {children}
    </section>
</NextAuthProvider>
```

That auth provider is a session provider, but contains an `AnonymousSessionProvider` that kicks in when there's no session.
```
<SessionProvider>
    <AnonymousSessionProvider>
        {children}
    </AnonymousSessionProvider>
</SessionProvider>
```

In `AnonymousSessionProvider` one hook pulls the session information, then a second does an anonymous 'sign-in' if there's no session.
```
  const {data: session, status} = useSession();
  useEffect(() => {
      if (status === "unauthenticated") {
          // login as anonymous
          signIn("credentials")
              .then((data) => {});
      }
  }, [status]);
```

In the back-end, the `/api/auth/[...nextauth]/route` has two providers:
```
export const authOptions: AuthOptions = {
    providers: [
        CredentialsProvider({
            name: "anonymous",
            credentials: {},
            async authorize(credentials, req) {
                return createAnonymousUser();
            },
        }),
        GithubProvider({
            clientId: process.env.GITHUB_CLIENT_ID as string,
            clientSecret: process.env.GITHUB_CLIENT_SECRET as string,
        }),
    ],
    callbacks: {
        async jwt({token, account, profile}: {token: JWT, account: Account | null, profile?: Profile}): Promise<JWT> {
            if (account && account?.expires_at && account?.type === 'oauth') {
                // at sign-in, persist in the JWT the GitHub account details to enable brokered requests in the future
                token.access_token = account.access_token;
                token.expires_at = account.expires_at;
                token.refresh_token = account.refresh_token;
                token.refresh_token_expires_in = account.refresh_token_expires_in;
                token.provider = 'github';
            }
            if (!token.provider) token.provider = 'anonymous';
            return token;
        },
        async session({session, token, user}: {session: Session, token: JWT, user: AdapterUser}): Promise<Session> {
            // don't make the token (JWT) contents available to the client session (JWT), but flag that they're server-side
            if (token.provider) {
                session.token_provider = token.provider;
            }
            return session;
        },
    },
    events: {
        async signIn({user, account, profile}: {user: User, account: Account | null, profile?: Profile}): Promise<void> {
            debug(`signIn of ${user.name} from ${user?.provider || account?.provider}`);
        },
        async signOut({session, token}: {session: Session, token: JWT}): Promise<void> {
            debug(`signOut of ${token.name} from ${token.provider}`);
        },
    },
    session: {
        // use default, an encrypted JWT (JWE) store in the session cookie
        strategy: "jwt" as SessionStrategy,
    },
}
const handler = NextAuth(authOptions);
```

and a helper function for creating a nice anonymous user:
```
const createAnonymousUser = (): User => {
    // generate a random name and email for this anonymous user
    const customConfig: Config = {
        dictionaries: [adjectives, colors, animals],
        separator: '-',
        length: 3,
        style: 'capital'
    };
    // handle is simple-red-aardvark
    const unique_handle: string = uniqueNamesGenerator(customConfig).replaceAll(' ','');
    // real name is Red Aardvark
    const unique_realname: string = unique_handle.split('-').slice(1).join(' ');
    const unique_uuid: string = randomUUID();
    return {
        id: unique_uuid,
        email: `${unique_handle.toLowerCase()}@example.com`,
        name: unique_realname,
        image: "",
        provider: "anonymous"
    };
};
```

This took a while to puzzle out from various blog posts and GitHub issues ([1](https://github.com/nextauthjs/next-auth/issues/568),[2](https://github.com/nextauthjs/next-auth/issues/6649)).  I hope that it helps anyone trying to do the same thing.  Please start with [the GitHub repo](https://github.com/lightenna/nextjs-app-auth-anon-logins-example), because the highlights shown in this blog post are illustrative only and not comprehensive, whereas the repo is complete and works at the time of writing.
