import { ApolloServer } from '@apollo/server';
import { startServerAndCreateNextHandler } from '@as-integrations/next';
import { gql } from 'graphql-tag';

// Define the GraphQL schema
const typeDefs = gql`
  type Query {
    hello: String
  }
`;

// Define the resolvers
const resolvers = {
  Query: {
    hello: () => 'Hello, world!',
  },
};

// Create the Apollo Server
const server = new ApolloServer({
  typeDefs,
  resolvers,
  introspection: true, // Enables the GraphQL Playground
});

// Export the default handler for Next.js API route
export default startServerAndCreateNextHandler(server);