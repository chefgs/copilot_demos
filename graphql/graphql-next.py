import os

# Define the base path for your Next.js project
base_path = os.path.join(os.getcwd(), 'nextjs-apollo')

# Folder structure to create
folders = [
    'src',
    'src/pages',
    'src/pages/about',
    'src/app/api/graphql'
]

# File contents
index_page_content = """export default function Home() {
  return (
    <div>
      <h1>Welcome to the Home Page</h1>
    </div>
  );
}
"""

about_page_content = """export default function About() {
  return (
    <div>
      <h1>About Us</h1>
    </div>
  );
}
"""

graphql_route_content = """import { ApolloServer } from 'apollo-server-micro';
import { gql } from 'graphql-tag';
import { NextApiRequest, NextApiResponse } from 'next';

// Define your GraphQL schema
const typeDefs = gql\`
  type Query {
    hello: String
  }
\`;

// Define your resolvers
const resolvers = {
  Query: {
    hello: () => 'hello world',
  },
};

// Create the Apollo Server
const apolloServer = new ApolloServer({ typeDefs, resolvers });
const startServer = apolloServer.start();

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  await startServer;
  await apolloServer.createHandler({ path: '/api/graphql' })(req, res);
}

export const config = {
  api: {
    bodyParser: false,
  },
};
"""

next_config_content = """/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  experimental: {
    appDir: true,
  },
}

module.exports = nextConfig
"""

# File paths and their corresponding contents
files = {
    'src/pages/index.tsx': index_page_content,
    'src/pages/about/index.tsx': about_page_content,
    'src/app/api/graphql/route.ts': graphql_route_content,
    'next.config.js': next_config_content,
}

def create_folders_and_files():
    # Create folders
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
    
    # Create files with content
    for file_path, content in files.items():
        file_full_path = os.path.join(base_path, file_path)
        with open(file_full_path, 'w') as f:
            f.write(content)
        print(f"Created file: {file_full_path}")

if __name__ == '__main__':
    create_folders_and_files()
