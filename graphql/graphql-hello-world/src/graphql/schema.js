import { gql } from 'graphql-tag';

// Define the GraphQL schema
const typeDefs = gql`
  type Query {
    hello: String
  }
`;

export default typeDefs;