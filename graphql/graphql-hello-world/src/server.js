const { ApolloServer } = require('@apollo/server');
const { startServerAndCreateNextHandler } = require('@as-integrations/next');
const typeDefs = require('./graphql/schema.js');
const resolvers = require('./graphql/resolvers.js');

// Create the Apollo Server
const server = new ApolloServer({
  typeDefs,
  resolvers,
  introspection: true, // Enables the GraphQL Playground
});

// Export the default handler for Next.js API route
export default startServerAndCreateNextHandler(server);