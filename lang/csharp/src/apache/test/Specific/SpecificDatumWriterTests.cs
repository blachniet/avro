using Avro.IO;
using Avro.Specific;
using NUnit.Framework;
using System;

namespace Avro.test.Specific
{
    [TestFixture]
    class SpecificDatumWriterTests
    {
        [TestCase(5, typeof(AvroTypeException))]
        [TestCase(null, typeof(ArgumentNullException))]
        public void TestSpecificDatumWriter_WriteFixed_BadValue(object value, Type expectedException)
        {
            var schema = Schema.Parse(@"{""type"":""record"",""name"":""MinimalSchema"",""fields"":[]}");
            var writer = new SampleSpecificDatumWriter<SampleSpecificRecord>(schema);
            Assert.Throws(expectedException, () =>
            {
                writer.TestInvokeWriteFixed(null, value, new BinaryEncoder());
            });
        }

        private class SampleSpecificRecord : ISpecificRecord
        {
            public Schema Schema => throw new NotImplementedException();

            public object Get(int fieldPos)
            {
                throw new NotImplementedException();
            }

            public void Put(int fieldPos, object fieldValue)
            {
                throw new NotImplementedException();
            }
        }

        private class SampleSpecificDatumWriter<T> : SpecificDatumWriter<T>
        {
            public SampleSpecificDatumWriter(Schema schema) : base(schema)
            {
            }

            public void TestInvokeWriteFixed(FixedSchema schema, object value, IO.Encoder encoder)
            {
                base.WriteFixed(schema, value, encoder);
            }
        }
    }
}
